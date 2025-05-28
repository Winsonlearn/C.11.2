from flask import Blueprint, render_template, jsonify, request, redirect, url_for, flash
from app.models import Element
from app import db
from app.forms import ElementForm
import json

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@main_bp.route('/index')
def index():
    elements = Element.query.order_by(Element.atomic_number).all()
    element_types_query = db.session.query(Element.element_type).distinct().filter(Element.element_type.isnot(None)).order_by(Element.element_type).all()
    element_types = [et[0] for et in element_types_query if et[0]]
    return render_template('index.html', title='Interactive Periodic Table', elements=elements, element_types=element_types)

@main_bp.route('/api/element/<int:atomic_number>', methods=['GET'])
def api_element_detail(atomic_number):
    element = Element.query.filter_by(atomic_number=atomic_number).first()
    if element:
        return jsonify({
            'atomic_number': element.atomic_number,
            'symbol': element.symbol,
            'name': element.name,
            'atomic_mass': element.atomic_mass,
            'group': element.group,
            'period': element.period,
            'element_type': element.element_type,
            'description': element.description,
            'appearance': element.appearance,
            'boil': element.boil,
            'density': element.density,
            'discovered_by': element.discovered_by,
            'melt': element.melt,
            'molar_heat': element.molar_heat,
            'named_by': element.named_by,
            'phase': element.phase,
            'source': element.source,
            'bohr_model_image': element.bohr_model_image,
            'bohr_model_3d': element.bohr_model_3d,
            'spectral_img': element.spectral_img,
            'xpos': element.xpos,
            'ypos': element.ypos,
            'shells': element.shells,
            'electron_configuration': element.electron_configuration,
            'electron_configuration_semantic': element.electron_configuration_semantic,
            'electron_affinity': element.electron_affinity,
            'electronegativity_pauling': element.electronegativity_pauling,
            'ionization_energies': element.ionization_energies,
            'cpk_hex': element.cpk_hex,
            'image_title': element.image_title,
            'image_url': element.image_url,
            'image_attribution': element.image_attribution,
            'block': element.block
        })
    else:
        return jsonify({'error': 'Element not found'}), 404

@main_bp.route('/element/new', methods=['GET', 'POST'])
def create_element():
    form = ElementForm()
    
    element_types_query = db.session.query(Element.element_type).distinct().filter(Element.element_type.isnot(None)).order_by(Element.element_type).all()
    form.element_type.choices = [('', 'Select Type (Optional)')] + [(et[0], et[0]) for et in element_types_query if et[0]]

    if form.validate_on_submit():
        new_element = Element(
            atomic_number=form.atomic_number.data,
            symbol=form.symbol.data,
            name=form.name.data,
            atomic_mass=form.atomic_mass.data,
            group=form.group.data,
            period=form.period.data,
            element_type=form.element_type.data if form.element_type.data else None,
            description=form.description.data,
            phase=form.phase.data,
            appearance=form.appearance.data,
            density=form.density.data,
            melt=form.melt.data,
            boil=form.boil.data,
            discovered_by=form.discovered_by.data,
            molar_heat=form.molar_heat.data,
            named_by=form.named_by.data,
            source=form.source.data
        )
        db.session.add(new_element)
        try:
            db.session.commit()
            flash(f'Element {new_element.name} added successfully!', 'success')
            return redirect(url_for('main.index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding element: {str(e)}', 'danger')
            
    return render_template('create_element.html', title='Add New Element', form=form)

@main_bp.route('/element/edit/<int:atomic_number>', methods=['GET', 'POST'])
def edit_element(atomic_number):
    element_to_edit = Element.query.filter_by(atomic_number=atomic_number).first_or_404()
    form = ElementForm(obj=element_to_edit)

    element_types_query = db.session.query(Element.element_type).distinct().filter(Element.element_type.isnot(None)).order_by(Element.element_type).all()
    form.element_type.choices = [('', 'Select Type (Optional)')] + [(et[0], et[0]) for et in element_types_query if et[0]]
    if element_to_edit.element_type and (element_to_edit.element_type, element_to_edit.element_type) not in form.element_type.choices:
        form.element_type.choices.append((element_to_edit.element_type, element_to_edit.element_type))

    if form.validate_on_submit():
        element_to_edit.symbol = form.symbol.data
        element_to_edit.name = form.name.data
        element_to_edit.atomic_mass = form.atomic_mass.data
        element_to_edit.group = form.group.data
        element_to_edit.period = form.period.data
        element_to_edit.element_type = form.element_type.data if form.element_type.data else None
        element_to_edit.description = form.description.data
        element_to_edit.phase = form.phase.data
        element_to_edit.appearance = form.appearance.data
        element_to_edit.density = form.density.data
        element_to_edit.melt = form.melt.data
        element_to_edit.boil = form.boil.data
        element_to_edit.discovered_by = form.discovered_by.data
        element_to_edit.molar_heat = form.molar_heat.data
        element_to_edit.named_by = form.named_by.data
        element_to_edit.source = form.source.data

        try:
            db.session.commit()
            flash(f'Element {element_to_edit.name} updated successfully!', 'success')
            return redirect(url_for('main.index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating element: {str(e)}', 'danger')
            
    return render_template('edit_element.html', title=f'Edit {element_to_edit.name}', form=form, element=element_to_edit)

@main_bp.route('/element/delete/<int:atomic_number>', methods=['POST'])
def delete_element(atomic_number):
    element_to_delete = Element.query.filter_by(atomic_number=atomic_number).first_or_404()
    try:
        db.session.delete(element_to_delete)
        db.session.commit()
        flash(f'Element {element_to_delete.name} deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting element: {str(e)}', 'danger')
    return redirect(url_for('main.index'))

@main_bp.route('/element/view/<int:atomic_number>')
def view_element(atomic_number):
    element = Element.query.filter_by(atomic_number=atomic_number).first_or_404()
    
    shells_list = []
    if element.shells:
        try:
            parsed_shells = json.loads(element.shells)
            if isinstance(parsed_shells, list):
                shells_list = parsed_shells
            else:
                shells_list = [str(parsed_shells)]
        except json.JSONDecodeError:
            shells_list = [element.shells]

    ionization_energies_list = []
    if element.ionization_energies:
        try:
            parsed_energies = json.loads(element.ionization_energies)
            if isinstance(parsed_energies, list):
                ionization_energies_list = parsed_energies
            else:
                ionization_energies_list = [str(parsed_energies)]
        except json.JSONDecodeError:
            ionization_energies_list = [element.ionization_energies]

    return render_template('element_view.html', 
                           title=element.name, 
                           element=element,
                           shells_data=shells_list,
                           ionization_energies_data=ionization_energies_list)

@main_bp.route('/elements')
def element_list():
    elements = Element.query.order_by(Element.atomic_number).all()
    return render_template('element_list.html', title='Manage Elements', elements=elements)

@main_bp.route('/compare', methods=['GET', 'POST'])
def compare_elements():
    elements = Element.query.order_by(Element.atomic_number).all()
    element_choices = [(e.atomic_number, f"{e.name} ({e.symbol})") for e in elements]

    selected_elements_data = []
    if request.method == 'POST':
        element_ids = request.form.getlist('elements_to_compare')
        if element_ids:
            for el_id in element_ids[:3]: 
                try:
                    element = Element.query.filter_by(atomic_number=int(el_id)).first()
                    if element:
                        selected_elements_data.append(element)
                except ValueError:
                    flash('Invalid element ID selected.', 'danger')
            if not selected_elements_data:
                flash('No valid elements selected for comparison or elements not found.', 'warning')
        else:
            flash('Please select at least two elements to compare.', 'info')
            
    return render_template('compare_elements.html', 
                           title='Compare Elements', 
                           elements=elements,
                           element_choices=element_choices,
                           selected_elements_data=selected_elements_data) 