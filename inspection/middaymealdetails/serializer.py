from rest_framework import serializers
from ..models import MidDayMealQuality


class MidDayMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = MidDayMealQuality
        fields = ('school_name', 'date', 'kit_shed', 'cond_kit_shed', 'loc', 'menu', 'fuel', 'shed_paint', 'enough_utensil',
                  'agency', 'clean_cooks', 'ingred', 'tasted', 'teacher_tasted', 'acc_menu', 'food_sealed', 'hand_wash',
                  'mothers_checked', 'panji', 'payment', 'food_right_price', 'food_stored', 'stored_food_good', 'teach_manage_part',
                  'milk_distributed', 'milk_powder', 'complaint', 'vit_tabs')