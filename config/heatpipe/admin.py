from django.contrib import admin

# Register your models here.
from .models import ItemSpec
 
class ItemSpecAdmin(admin.ModelAdmin):
    search_fields = ['itemcode_text']
    exclude = ['content']
    list_display = ('itemcode_text', 'client_text', 'project_text', 'type_text', 'heat_dissipate_deci', 'delta_temp_deci', 'rth_deci', 'ambient_intf', 'ambient_intt', 'weight_deci', 'pipe_num_int', 'fins_num_int')
    
admin.site.register(ItemSpec, ItemSpecAdmin)
