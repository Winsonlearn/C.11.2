import os
import re

# Define model mappings
model_mappings = {
    'KotaModel': 'Kota',
    'KategoriModel': 'Kategori',
    'PenjualModel': 'Penjual',
    'ProductModel': 'Product',
    'ProductDetailsModel': 'ProductDetails',
    'KategoriPenjualModel': 'KategoriPenjual'
}

# Define method mappings
method_mappings = {
    'get_all_kota': 'get_all',
    'get_kota_by_id': 'get_by_id',
    'insert_kota': 'create',
    'update_kota': 'update',
    'delete_kota': 'delete',
    
    'get_all_kategori': 'get_all',
    'get_kategori_by_id': 'get_by_id',
    'insert_kategori': 'create',
    'update_kategori': 'update',
    'delete_kategori': 'delete',
    
    'get_all_penjual': 'get_all',
    'get_penjual_by_id': 'get_by_id',
    'insert_penjual': 'create',
    'update_penjual': 'update',
    'delete_penjual': 'delete',
    
    'get_all_products': 'get_all',
    'get_product_by_id': 'get_by_id',
    'insert_product': 'create',
    'update_product': 'update',
    'delete_product': 'delete',
    
    'get_all_product_details': 'get_all',
    'get_product_details_by_id': 'get_by_id',
    'insert_product_details': 'create',
    'update_product_details': 'update',
    'delete_product_details': 'delete',
    
    'get_all_kategori_penjual': 'get_all',
    'get_kategori_penjual_by_id': 'get_by_id',
    'insert_kategori_penjual': 'create',
    'update_kategori_penjual': 'update',
    'delete_kategori_penjual': 'delete'
}

controllers_dir = 'app/controllers'

# Process each controller file
for filename in os.listdir(controllers_dir):
    if filename.endswith('.py'):
        filepath = os.path.join(controllers_dir, filename)
        with open(filepath, 'r') as file:
            content = file.read()
        
        # Update imports
        for old_model, new_model in model_mappings.items():
            content = re.sub(
                f'from app.models\\.(\\w+)_model import {old_model}',
                f'from app.models.\\1_model import {new_model}',
                content
            )
        
        # Remove model instantiation
        for old_model in model_mappings.keys():
            content = re.sub(
                f'{old_model}\\(\\)',
                '',
                content
            )
        
        # Update method calls
        for old_method, new_method in method_mappings.items():
            for old_model, new_model in model_mappings.items():
                # Convert assignments like: variable = model_instance.old_method(args)
                pattern = f'(\\s+)([\\w\\d_]+)\\s*=\\s*([\\w\\d_]*)\\s*\\.\\s*{old_method}\\s*\\(([^)]*)\\)'
                replacement = f'\\1\\2 = {new_model}.{new_method}(\\4)'
                content = re.sub(pattern, replacement, content)
                
                # Convert standalone calls like: model_instance.old_method(args)
                pattern = f'([\\w\\d_]*)\\s*\\.\\s*{old_method}\\s*\\(([^)]*)\\)'
                replacement = f'{new_model}.{new_method}(\\2)'
                content = re.sub(pattern, replacement, content)
        
        # Add object-oriented updates
        # For update operations
        for old_model, new_model in model_mappings.items():
            if 'update' in content and f'{new_model}.update' in content:
                # Look for direct update calls and convert to object-oriented style
                pattern = f'{new_model}\\.update\\((\\w+)\\s*,\\s*([^)]*)\\)'
                replacement = f'{new_model}.get_by_id(\\1).update(\\2) if {new_model}.get_by_id(\\1) else None'
                content = re.sub(pattern, replacement, content)
                
            if 'delete' in content and f'{new_model}.delete' in content:
                # Look for direct delete calls and convert to object-oriented style
                pattern = f'{new_model}\\.delete\\((\\w+)\\)'
                replacement = f'{new_model}.get_by_id(\\1).delete() if {new_model}.get_by_id(\\1) else None'
                content = re.sub(pattern, replacement, content)
        
        # Write the modified content back to the file
        with open(filepath, 'w') as file:
            file.write(content)

print("All controllers have been updated to use ORM!") 