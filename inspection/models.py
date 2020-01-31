from django.db import models


class SchoolSelfies(models.Model):
    sch_selfie = models.ImageField(upload_to='images/')
    object = models.Manager()


class SchoolMaster(models.Model):
    school_code = models.IntegerField(primary_key=True)
    diascode = models.CharField(max_length=50, null=True)
    school_nm_e = models.CharField(max_length=100, null=True)
    school_nm_h = models.CharField(max_length=100, null=True)
    dist_cd = models.CharField(max_length=100, null=True)
    dist_nm = models.CharField(max_length=100, null=True)
    b_cd = models.CharField(max_length=100, null=True)
    block_nm_e = models.CharField(max_length=100, null=True)
    block_nm_h = models.CharField(max_length=100, null=True)
    gp_cd = models.CharField(max_length=100, null=True)
    gp_nm_h = models.CharField(max_length=100, null=True)
    gp_nm_e = models.CharField(max_length=100, null=True)
    vill_cd = models.CharField(max_length=100, null=True)
    vill_nm_h = models.CharField(max_length=100, null=True)
    vill_nm_e = models.CharField(max_length=100, null=True)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    object = models.Manager()


class surveyor_registration(models.Model):
    surveyor_name = models.CharField(max_length=500, null=True)
    surveyor_designation = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=11, null=True)
    object = models.Manager()


class HRTeachers(models.Model):
    school_name = models.CharField(max_length=500, null=True)
    date = models.CharField(max_length=500, null=True)
    teacher_name = models.CharField(max_length=500, null=True)
    teacher_designation = models.CharField(max_length=100, null=True)
    attendance = models.CharField(max_length=100, null=True)
    reason = models.CharField(max_length=100, null=True)
    object = models.Manager()


class InfrastructureDetails(models.Model):
    school_name = models.CharField(max_length=500, null=True)
    date = models.CharField(max_length=500, null=True)
    building = models.CharField(max_length=500, null=True)
    terrace = models.CharField(max_length=500, null=True)
    numRooms = models.CharField(max_length=500, null=True)
    enoughRooms = models.CharField(max_length=500, null=True)
    seats = models.CharField(max_length=500, null=True)
    toilet = models.CharField(max_length=500, null=True)
    cleanToilet = models.CharField(max_length=500, null=True)
    waterInToilet = models.CharField(max_length=500, null=True)
    approachRoad = models.CharField(max_length=500, null=True)
    roadType = models.CharField(max_length=500, null=True)
    waterSrc = models.CharField(max_length=500, null=True)
    boundary = models.CharField(max_length=500, null=True)
    ground = models.CharField(max_length=500, null=True)
    powerCon = models.CharField(max_length=500, null=True)
    object = models.Manager()


class Students(models.Model):
    school_name = models.CharField(max_length=500, null=True)
    date = models.CharField(max_length=500, null=True)
    standard = models.CharField(max_length=500, null=True)
    enrolled = models.CharField(max_length=500, null=True)
    present = models.CharField(max_length=500, null=True)
    object = models.Manager()


class TeachingQuality(models.Model):
    school_name = models.CharField(max_length=500, null=True)
    date = models.CharField(max_length=500, null=True)
    standard = models.CharField(max_length=500, null=True)
    syll_status = models.CharField(max_length=500, null=True)
    lang_level = models.CharField(max_length=500, null=True)
    math_level = models.CharField(max_length=500, null=True)
    gen_level = models.CharField(max_length=500, null=True)
    object = models.Manager()


class MidDayMealQuality(models.Model):
    school_name = models.CharField(max_length=500, null=True)
    date = models.CharField(max_length=500, null=True)
    kit_shed = models.CharField(max_length=500, null=True)
    cond_kit_shed = models.CharField(max_length=500, null=True)
    loc = models.CharField(max_length=500, null=True)
    menu = models.CharField(max_length=500, null=True)
    fuel = models.CharField(max_length=500, null=True)
    shed_paint = models.CharField(max_length=500, null=True)
    enough_utensil = models.CharField(max_length=500, null=True)
    agency = models.CharField(max_length=500, null=True)
    clean_cooks = models.CharField(max_length=500, null=True)
    ingred = models.CharField(max_length=500, null=True)
    tasted = models.CharField(max_length=500, null=True)
    teacher_tasted = models.CharField(max_length=500, null=True)
    acc_menu = models.CharField(max_length=500, null=True)
    food_sealed = models.CharField(max_length=500, null=True)
    hand_wash = models.CharField(max_length=500, null=True)
    mothers_checked = models.CharField(max_length=500, null=True)
    panji = models.CharField(max_length=500, null=True)
    payment = models.CharField(max_length=500, null=True)
    food_right_price = models.CharField(max_length=500, null=True)
    food_stored = models.CharField(max_length=500, null=True)
    stored_food_good = models.CharField(max_length=500, null=True)
    teach_manage_part = models.CharField(max_length=500, null=True)
    milk_distributed = models.CharField(max_length=500, null=True)
    milk_powder = models.CharField(max_length=500, null=True)
    complaint = models.CharField(max_length=500, null=True)
    vit_tabs = models.CharField(max_length=500, null=True)
    object = models.Manager()


class MDMDataDetails(models.Model):
    sn = models.IntegerField(null=True)
    dCode = models.CharField(max_length=500, null=True)
    schName = models.CharField(max_length=500, null=True)
    devBlk = models.CharField(max_length=500, null=True)
    agencyName = models.CharField(max_length=500, null=True)
    object = models.Manager()


class MDMData(models.Model):
    school_name = models.CharField(max_length=500, null=True)
    date = models.CharField(max_length=500, null=True)
    agencyName = models.CharField(max_length=500, null=True)
    numMem = models.CharField(max_length=500, null=True)
    presName = models.CharField(max_length=500, null=True)
    secName = models.CharField(max_length=500, null=True)
    object = models.Manager()


class TeachersDetails(models.Model):
    sn = models.IntegerField(null=True)
    schName = models.CharField(max_length=500, null=True)
    tName = models.CharField(max_length=500, null=True)
    desig = models.CharField(max_length=500, null=True)
    object = models.Manager()