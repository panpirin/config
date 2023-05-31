from django.db import models

# Create your models here.
class ItemSpec(models.Model):
		prodcode_text = models.CharField(max_length=200, blank=True)   # Product Code
		itemcode_text = models.CharField(max_length=50)    # 품목 코드
		drowcode_text = models.CharField(max_length=200, blank=True)   # drowcode_text
		type_text = models.CharField(max_length=10, blank=True)        # 품목 Type
		heat_dissipate_deci = models.DecimalField(max_digits=10, decimal_places=3)  # Heat Dissipate (kW)
		delta_temp_deci = models.DecimalField(max_digits=8, decimal_places=2)  # Delta Temperature (K)
		rth_deci = models.DecimalField(max_digits=8, decimal_places=5)  # Rth
		cooling_text = models.CharField(max_length=50, blank=True)   # Coolng (m/s)
		ambient_intf = models.IntegerField() # Ambient_from (℃)
		ambient_intt = models.IntegerField() # Ambient_to (℃)
		weight_deci = models.DecimalField(max_digits=8, decimal_places=2) # Weight (kg)	
		size_text = models.CharField(max_length=100, blank=True)   # Size (mm)
		basesize_text = models.CharField(max_length=100, blank=True)   # Base Size
		mold_text = models.CharField(max_length=30, blank=True)   # 금형 보유
		product_type_text = models.CharField(max_length=50, blank=True)   # Product Types
		pipe_num_int = models.IntegerField() # Number of Pipes
		fins_num_int = models.IntegerField() # Number of Fins
		client_text  = models.CharField(max_length=200, blank=True)   # Name of Clients	
		project_text = models.CharField(max_length=300, blank=True)   # Name of Project
		content = models.TextField(blank=True) # Content
		create_date = models.DateTimeField(blank=True)   # create date

		def __str__(self): 
			return self.itemcode_text