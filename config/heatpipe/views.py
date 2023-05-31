from django.shortcuts import render 
from .models import ItemSpec
from django.core.paginator import Paginator   
from django.db.models import Q   # 검색기능 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def post_new(request):
    [...]
# (login_url='/common/login/')

def index(request):
    page = request.GET.get('page', '1')  # 페이지
    search_item = request.GET.get('search_item', '')  
    search_type = request.GET.get('search_type', 'ALL')  
    search_detat = request.GET.get('search_detat', 'ALL') 
    search_cooling = request.GET.get('search_cooling', 'ALL')  
    search_ambient = request.GET.get('search_ambient', '')  
    search_weight = request.GET.get('search_weight', '')  
    search_mold = request.GET.get('search_mold', 'ALL')  
    search_pipenum = request.GET.get('search_pipenum', '') 
    search_finnum = request.GET.get('search_finnum', '') 
    search_client = request.GET.get('search_client', '')  
    search_dissipate = request.GET.get('search_dissipate', '') 

    if search_ambient:
        search_ambient_int = int(search_ambient)
    else:
        search_ambient_int = 0
    
    if search_detat != 'ALL':
        search_detat_f = float(search_detat) - 10
        search_detat_t = float(search_detat) 
    else:
        search_detat_f = 0 
        search_detat_t = 100

    if search_weight:
        search_weight_float = float(search_weight)
    else:
        search_weight_float = 500 

    if search_pipenum:
        search_pipenum_int = int(search_pipenum)
    else:
        search_pipenum_int = 1000

    if search_finnum:
        search_finnum_int = int(search_finnum)
    else:
        search_finnum_int = 1000

    if search_dissipate:
        search_dissipate_f = float(search_dissipate)
        search_dissipate_t = float(search_dissipate) + 0.99 
    # Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) 


    itemspec_list = ItemSpec.objects.order_by('-itemcode_text')
    # if search_item: 
    #     itemspec_list = itemspec_list.filter(
    #             Q(itemcode_text__icontains=search_item)   # Item Code 검색 And 연산 &  OR 연산  |
    #         # Q(type_text_text__icontains=type) |   Type 검색
    #         # Q(client_text__icontains=search_item) |   Name of Clients 검색
    #         # Q(project_text__icontains=search_item)  # Name of Project	 검색
    #         #  Q(answer__author__username__icontains=search_item)  답변 글쓴이 검색
    #         ).distinct() 
      
    if search_item:
        itemspec_list = itemspec_list.filter(Q(itemcode_text__icontains=search_item))    
        if search_type != 'ALL':
            if search_cooling != 'ALL':
                if search_ambient:
                    if search_mold != 'ALL':
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                            Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) &
                                            Q(mold_text__icontains=search_mold) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) &
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                            Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                            Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) &
                                            Q(mold_text__icontains=search_mold) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) &
                                            Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate: 
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                            Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) &
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                            Q(mold_text__icontains=search_mold) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                            Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) &
                                            Q(mold_text__icontains=search_mold) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                    else: 
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) &
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) &
                                        Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                else: 
                    if search_mold != 'ALL':
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                        Q(mold_text__icontains=search_mold) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) &
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                        Q(mold_text__icontains=search_mold) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) &
                                        Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate: 
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(mold_text__icontains=search_mold) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                temspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                        Q(mold_text__icontains=search_mold) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                    else:
                        if search_client:
                            if search_dissipate: 
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) &
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) &
                                        Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) & 
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
            else:
                if search_ambient:
                    if search_mold != 'ALL':
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(weight_deci__lte=search_weight_float) & 
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(weight_deci__lte=search_weight_float) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(weight_deci__lte=search_weight_float) & 
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(weight_deci__lte=search_weight_float) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                    else:
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(weight_deci__lte=search_weight_float) &
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(weight_deci__lte=search_weight_float) &
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(weight_deci__lte=search_weight_float) &
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(weight_deci__lte=search_weight_float) &
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                else:
                    if search_mold != 'ALL':
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) & Q(mold_text__icontains=search_mold) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) & Q(mold_text__icontains=search_mold) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) & Q(mold_text__icontains=search_mold) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) & Q(mold_text__icontains=search_mold) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                    else:
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                    Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                    Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                    Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                    Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                    Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                    Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                    Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                    Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                    Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                    Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                    Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                    Q(itemcode_text__icontains=search_item) & Q(type_text__icontains=search_type) &
                                    Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                    Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
        else:   
            if search_cooling != 'ALL':
                if search_ambient:
                    if search_mold != 'ALL':
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & Q(mold_text__icontains=search_mold) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                            Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & Q(mold_text__icontains=search_mold) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                            Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & Q(mold_text__icontains=search_mold) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                            Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & Q(mold_text__icontains=search_mold) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                            Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                    else:
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                            Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                            Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                            Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                            Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                else:
                    if search_mold != 'ALL':
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & Q(mold_text__icontains=search_mold) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) & 
                                            Q(cooling_text__startswith=search_cooling) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) &
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                            Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & Q(mold_text__icontains=search_mold) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) & 
                                            Q(cooling_text__startswith=search_cooling) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) &
                                            Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & Q(mold_text__icontains=search_mold) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) & 
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                            Q(cooling_text__startswith=search_cooling) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else: 
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & Q(mold_text__icontains=search_mold) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) & 
                                            Q(cooling_text__startswith=search_cooling) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                    else:
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) & 
                                            Q(cooling_text__startswith=search_cooling) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & 
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                            Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) & 
                                            Q(cooling_text__startswith=search_cooling) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & 
                                            Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) & 
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                            Q(cooling_text__startswith=search_cooling) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else: 
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) & 
                                            Q(cooling_text__startswith=search_cooling) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
            else:
                if search_ambient:
                    if search_mold != 'ALL':
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(pipe_num_int__lte=search_pipenum_int) &
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) & 
                                            Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(pipe_num_int__lte=search_pipenum_int) & 
                                            Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(pipe_num_int__lte=search_pipenum_int) & 
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                            Q(fins_num_int__lte=search_finnum_int))    
                            else:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(pipe_num_int__lte=search_pipenum_int) & 
                                            Q(fins_num_int__lte=search_finnum_int))  
                    else:
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & Q(mold_text__icontains=search_mold) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(pipe_num_int__lte=search_pipenum_int) & 
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                            Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & Q(mold_text__icontains=search_mold) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(pipe_num_int__lte=search_pipenum_int) & 
                                            Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & Q(mold_text__icontains=search_mold) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(pipe_num_int__lte=search_pipenum_int) & 
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                            Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                            Q(itemcode_text__icontains=search_item) & Q(mold_text__icontains=search_mold) & 
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(pipe_num_int__lte=search_pipenum_int) & 
                                            Q(fins_num_int__lte=search_finnum_int))
                else:
                    if search_mold != 'ALL': 
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) & 
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                            else: 
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) & 
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                    else:
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) &
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(itemcode_text__icontains=search_item) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) &
                                        Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                    Q(itemcode_text__icontains=search_item) & Q(weight_deci__lte=search_weight_float) &
                                    Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(pipe_num_int__lte=search_pipenum_int) & 
                                    Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                    Q(fins_num_int__lte=search_finnum_int))
                            else: 
                                itemspec_list = itemspec_list.filter(
                                    Q(itemcode_text__icontains=search_item) & Q(weight_deci__lte=search_weight_float) &
                                    Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(pipe_num_int__lte=search_pipenum_int) & 
                                    Q(fins_num_int__lte=search_finnum_int))
    else: # search_item is null 
        itemspec_list = itemspec_list.exclude(Q(itemcode_text__isnull=True) | Q(itemcode_text__exact=''))
        if search_type != 'ALL': 
            if search_cooling != 'ALL':
                if search_ambient:
                    if search_mold != 'ALL':
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(type_text__icontains=search_type) & Q(mold_text__icontains=search_mold) &
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                            Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) &
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                            Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                            Q(type_text__icontains=search_type) & Q(mold_text__icontains=search_mold) &
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                            Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) &
                                            Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(type_text__icontains=search_type) & Q(mold_text__icontains=search_mold) &
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                            Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else: 
                                itemspec_list = itemspec_list.filter(
                                            Q(type_text__icontains=search_type) & Q(mold_text__icontains=search_mold) &
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                            Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                    else:
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & 
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) &
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & 
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) &
                                        Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & 
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & 
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                else: 
                    if search_mold != 'ALL':
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(mold_text__icontains=search_mold) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & 
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(client_text__icontains=search_client))
                            else: 
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(mold_text__icontains=search_mold) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & 
                                        Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(mold_text__icontains=search_mold) & 
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(mold_text__icontains=search_mold) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                    else:
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(pipe_num_int__lte=search_pipenum_int) &
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) & 
                                        Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                            else: 
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(pipe_num_int__lte=search_pipenum_int) & 
                                        Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) & 
                                        Q(cooling_text__startswith=search_cooling) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
            else:
                if search_ambient:
                    if search_mold != 'ALL':
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & 
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) & 
                                            Q(client_text__icontains=search_client))
                            else: 
                                itemspec_list = itemspec_list.filter(
                                            Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & 
                                            Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) & 
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                            Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                    else:
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & 
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) & 
                                            Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                            Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & 
                                            Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                else:
                    if search_mold != 'ALL':
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) & 
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                            else: 
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) & 
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else: 
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                    else:
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) &
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(client_text__icontains=search_client))
                            else: 
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) &
                                        Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & 
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(type_text__icontains=search_type) & Q(weight_deci__lte=search_weight_float) &
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
        else:
            if search_cooling != 'ALL':
                if search_ambient:
                    if search_mold != 'ALL':
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) &   
                                            Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) & 
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) &   
                                            Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) & 
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) &   
                                            Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) & 
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else: 
                                itemspec_list = itemspec_list.filter(
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) &   
                                            Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) & 
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                    else:
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                            else: 
                                itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) & 
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                else:
                    if search_mold != 'ALL':
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) )
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) )
                    else:
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &   
                                        Q(cooling_text__startswith=search_cooling) & Q(weight_deci__lte=search_weight_float) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
            else:
                if search_ambient:
                    if search_mold != 'ALL':
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(mold_text__icontains=search_mold) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                    else:
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & 
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) &
                                        Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & 
                                        Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) &
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                 itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                else:
                    # itemspec_list = itemspec_list.exclude(Q(itemcode_text__isnull=True) | Q(itemcode_text__exact=''))
                    if search_mold != 'ALL':
                        if search_client:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(mold_text__icontains=search_mold) & 
                                            Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) & 
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                            else:
                                itemspec_list = itemspec_list.filter(
                                            Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                            Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(mold_text__icontains=search_mold) & 
                                            Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(mold_text__icontains=search_mold) & 
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & Q(mold_text__icontains=search_mold) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                    else:
                        if search_client: 
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                            else: 
                                itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int) & Q(client_text__icontains=search_client))
                        else:
                            if search_dissipate:
                                itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                        Q(heat_dissipate_deci__gte=search_dissipate_f, heat_dissipate_deci__lte=search_dissipate_t) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                            else:
                                itemspec_list = itemspec_list.filter(
                                        Q(delta_temp_deci__gte=search_detat_f, delta_temp_deci__lte=search_detat_t) & Q(weight_deci__lte=search_weight_float) &
                                        Q(ambient_intf__lte=search_ambient_int) & Q(ambient_intt__gte=search_ambient_int) & 
                                        Q(pipe_num_int__lte=search_pipenum_int) & Q(fins_num_int__lte=search_finnum_int))
                              


    paginator = Paginator(itemspec_list, 100)  # 페이지당 100개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'itemspec_list': page_obj, 'page': page, 
               'search_item': search_item, 
               'search_type': search_type, 
               'search_detat': search_detat, 
               'search_cooling': search_cooling,
               'search_ambient': search_ambient,
               'search_weight': search_weight,
               'search_mold': search_mold,
               'search_pipenum': search_pipenum,
               'search_finnum': search_finnum,
               'search_client': search_client,
               'search_dissipate': search_dissipate
               }
    # context = {'itemspec_list': page_obj, 'search': search_item}
    # context = {'itemspec_list': itemspec_list}
    return render(request, 'templates/heatpipe/itemspec_list.html', context)


def detail(request, itemspec_list_id):
    itemspec_list = ItemSpec.objects.get(id=itemspec_list_id)
    # itemspec_list = get_object_or_404(itemspec_list, pk=itemspec_list_id)
    context = {'itemspec_list': itemspec_list}
    return render(request, 'templates/heatpipe/itemspec_list_detail.html', context)
 
  