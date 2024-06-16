"""
I would like to make a program that makes my job easier.
I currently work as a clinical research coordinator in
ophthalmology. We have a few new studies that we have
started working on so I'd like to make a program that a series
of questions about patient data and then prints that data
back to the user and matches them to one of the studies
OR states why they met exclusion criteria.
"""

def line_break():
    print(" ")

def exclusion_criteria():
    line_break()
    exclusion_criteria_promopt = print("Based on the data entered, this patient is excluded from the GMOPC study.")
    exit()

def intro():
    print("Welcome to the GMOPC Research Study Matcher.")
    print("I'm going to ask a series of questions about patient data.")
    print("Some of the answers may seem obvious, but it's simply in the sake of clarity.")
    print("Let's begin: ")
    line_break()

def visual_acuity():
    cor_vis_ac = int(input("Enter the patient's best corrected visual acuity: 20/"))
    if cor_vis_ac >= 40:
        exclusion_criteria()
    line_break()

def acqr_rfrx():
    # Take refraction as input
    sphere_power = float(input("Enter the sphere power (include negative sign, if applicable): "))
    cylinder_power = float(input("Enter the cylinder power (include negative sign, if applicable): "))
    axis_degrees = int(input("Enter the axis in degrees: "))
    line_break()
    return sphere_power, cylinder_power, axis_degrees

def cyl_conv(sphere_power, cylinder_power, axis_degrees):
    # If refraction input is in plus-cylinder, convert to minus-cylinder.
    # Else, assign the negative cylinder powers to the correct variable.
    if cylinder_power >= 0.00:
        sph_pow_neg_cyl = sphere_power + cylinder_power
        neg_cyl_pow = -cylinder_power
        # Convert axis degrees
        if axis_degrees >= 90:
            neg_cyl_axis_deg = axis_degrees - 90
        else:
            neg_cyl_axis_deg = axis_degrees + 90
    else:
        sph_pow_neg_cyl = sphere_power
        neg_cyl_pow = cylinder_power
        neg_cyl_axis_deg = axis_degrees
    print("This patient's negative-cylinder refraction is: " +
          "S:" + str(sph_pow_neg_cyl) + "  " +
          "C:" + str(neg_cyl_pow) + "  " +
          "A:" + str(neg_cyl_axis_deg))
    print("Checking criteria based on astigmatism...")
    astig = neg_cyl_pow * -1
    print("Patient's astigmatism/cylinder is: " + str(astig))
    if astig > 3.00:
        exclusion_criteria()
    return sph_pow_neg_cyl, neg_cyl_pow

def calc_sph_eq(sph_pow_neg_cyl, neg_cyl_pow):
    # Spherical equivalent conversion is: SE = (S + (C/2))
    # cyl_pow_conv = cylinder_power
    spherical_equivalent = sph_pow_neg_cyl + (neg_cyl_pow/2)
    print("This patient's spherical equivalent is: " + str(spherical_equivalent) + "\n")
    return spherical_equivalent

def io_sx_prompts():
    io_sx = str(input("Has this patient had any intraocular surgery beyond cataract/IOL, refractive, or any glaucoma surgery (Y/N)? "))
    if io_sx == "N" or io_sx == "n":
        io_sx_2 = str(input("Has this patient had scleral buckling surgery (Y/N)? "))
        if io_sx_2 == "N" or io_sx_2 == "n":
            io_sx_3 = str(input("Has this patient had recent use of orthokeratology lenses (Y/N)? "))
            if io_sx_3 == "N" or io_sx_3 == "n":
                pass
            else:
                exclusion_criteria()
        else:
            exclusion_criteria()
    else:
        exclusion_criteria()

def cohort_1_prompts():
    print("This patient might be a candidate for Cohort 1.")
    print("But first we'll need some more information: ")
    line_break()
    io_sx_prompts()
    iop_od_c1 = int(input("Enter the patient's IOP for their right eye: "))
    iop_os_c1 = int(input("Enter the patient's IOP for their left eye: "))
    if iop_os_c1 or iop_od_c1 >= 22:
        exclusion_criteria()
    else:
        line_break()
        print("Upon initial review, this patient appears to meet GMOPC Cohort 1 criteria!")

def cohort_2_prompts():
    print("This patient might be a candidate for Cohort 2.")
    print("But first we'll need some more information: ")
    line_break()
    io_sx_prompts()
    glauc_optic_neuropathy = str(input("Does this patient have clinically identifiable focal thinning or notching of the ONH rim tissue and/or adjacent ppRNFL bundle defects (Y/N)? "))
    if glauc_optic_neuropathy == "Y" or glauc_optic_neuropathy == "y":
        hfa_cohort_2 = str(input('Does this patient have 24-2 HFA abnormalities on 2 or more testing instances ("borderline" or "ONL" AND a pattern deviation (PD) plot with a cluster >= 3 below 5%, at least 1 of which is below 1%, in an expected location) (Y/N)? '))
        if hfa_cohort_2 == "Y" or hfa_cohort_2 == "y":
            line_break()
            print("Upon initial review, this patient appears to meet GMOPC Cohort 2 criteria!")
        else:
            exclusion_criteria()
    else:
        exclusion_criteria()

def cohort_3_q9():
    onh_rim_c3 = str(input('Does this patient have focal thinning or notching of the ONH rim tissue and adjacent peripapillary or macular RNFL bundle defects that appear glaucomatous or are considered glaucomatous-suspicious and that are in the appropriate ONH or retinal hemisphere (Y/N)? '))
    if onh_rim_c3 == "Y" or onh_rim_c3 == "y":
        line_break()
        print("Upon initial review, this patient appears to meet GMOPC Cohort 3 criteria!")
    else:
        exclusion_criteria()

def cohort_3_prompts():
    print("This patient might be a candidate for Cohort 3.")
    print("But first we'll need some more information: ")
    line_break()
    io_sx_prompts()
    mean_deviation = int(input("What was the mean deviation (MD) in dB on this patient's 24-2 HFA? "))
    if mean_deviation >= -6:
        hfa_defects_c3 = str(input("Did this patient's 24-2 HFA test as 'borderline' or 'ONL' (Y/N)? "))
        if hfa_defects_c3 == "Y" or hfa_defects_c3 == "y":
            cohort_3_q9()
        else:
            hfa_10_2_c3 = str(input("Did this patient show 10-2 HFA defects of contiguous test points in one hemifield with total deviation points falling below 5th percentile of normal distribution (Y/N)? "))
            if hfa_10_2_c3 == "Y" or hfa_10_2_c3 == "y":
                cohort_3_q9()
            else:
                exclusion_criteria()
    else:
        exclusion_criteria()

def myopia_status(spherical_equivalent):
    # Determine if pt is myopic or not
    if spherical_equivalent <= -6.00:
        # If yes: Diagnosis of glaucoma or not?
        glaucoma_dx = str(input("Has this patient been formally diagnosed with glaucoma (Y/N)? "))
        # If yes: Questions about Cohort 2
        if glaucoma_dx == "Y" or glaucoma_dx == "y":
            cohort_2_prompts()

        # if no: Questions about Cohort 1
        else:
            cohort_1_prompts()

    # If no: Verify axial length:
    else:
        pt_axial_length = float(input("Please enter the patient's axial length: "))
        line_break()
        # If axial length is greater than 26: Question about glaucoma -> follow the question set above
        if pt_axial_length >= 26.00:
            glaucoma_dx = str(input("Has this patient been formally diagnosed with glaucoma (Y/N)? "))
            line_break()
            # If yes: Questions about Cohort 2
            if glaucoma_dx == "Y" or glaucoma_dx == "y":
                cohort_2_prompts()

            # if no: Questions about Cohort 1
            else:
                cohort_1_prompts()

        # If axial length is less than 26: Questions about Cohort 3
        else:
            cohort_3_prompts()


def main():
    intro()
    visual_acuity()
    sphere_power, cylinder_power, axis_degrees = acqr_rfrx()
    sph_pow_neg_cyl, neg_cyl_pow = cyl_conv(sphere_power, cylinder_power, axis_degrees)
    spherical_equivalent = calc_sph_eq(sph_pow_neg_cyl, neg_cyl_pow)
    myopia_status(spherical_equivalent)

if __name__ == '__main__':
    main()