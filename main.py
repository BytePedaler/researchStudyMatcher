"""
I would like to make a program that makes my job easier.
I currently work as a clinical research coordinator in
ophthalmology. We have a few new studies that we have
started working on so I'd like to make a program that a series
of questions about patient data and then prints that data
back to the user and matches them to one of the studies
OR states why they met exclusion criteria.
"""

def intro():
    print("Welcome to the GMOPC Research Study Matcher.")
    print("I'm going to ask a series of questions about patient data.")
    print("Some of the answers may seem obvious, but it's simply in the sake of clarity.")
    print("Let's begin: ")

def acqr_rfrx():
    # Take refraction as input
    sphere_power = float(input("Enter the sphere power (include negative sign, if applicable): "))
    cylinder_power = float(input("Enter the cylinder power (include negative sign, if applicable): "))
    axis_degrees = int(input("Enter the axis in degrees: "))
    print(" ")
    return sphere_power, cylinder_power, axis_degrees

def cyl_conv():
    sphere_power, cylinder_power, axis_degrees = acqr_rfrx()
    # If refraction input is in plus-cylinder, convert to minus-cylinder.
    # Else, assign the negative cylinder powers to the correct variable.
    if cylinder_power >= 0.00:
        sph_pow_neg_cyl = sphere_power + cylinder_power
        neg_cyl_pow = 0.00 - cylinder_power
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
    return sph_pow_neg_cyl, neg_cyl_pow, neg_cyl_axis_deg

def calc_sph_eq():
    sph_pow_neg_cyl, neg_cyl_pow, neg_cyl_axis_deg = cyl_conv()
    # Spherical equivalent conversion is: SE = (S + (C/2))
    # cyl_pow_conv = cylinder_power
    spherical_equivalent = (sph_pow_neg_cyl + (neg_cyl_pow/2))
    print("This patient's spherical equivalent is: " + str(spherical_equivalent))
    print(" ")
    return spherical_equivalent

def myopia_status():
    spherical_equivalent = calc_sph_eq()
    # Determine if pt is myopic or not
    if spherical_equivalent <= -6.00:
        # If yes: Diagnosis of glaucoma or not?
        glaucoma_dx = str(input("Has this patient been formally diagnosed with glaucoma (Y/N)? "))
        # If yes: Questions about Cohort 2
        if glaucoma_dx == "Y":
            pass

        # if no: Questions about Cohort 1
        else:
            pass

    # If no: Verify axial length:
    else:
        pt_axial_length = float(input("Please enter the patient's axial length: "))
        # If axial length is greater than 26: Question about glaucoma -> follow the question set above
        if pt_axial_length >= 26.00:
            glaucoma_dx = str(input("Has this patient been formally diagnosed with glaucoma (Y/N)? "))
            # If yes: Questions about Cohort 2
            if glaucoma_dx == "Y":
                pass

            # if no: Questions about Cohort 1
            else:
                pass

        # If axial length is less than 26: Questions about Cohort 3
        else:
            pass


def main():
    intro()
    myopia_status()

if __name__ == '__main__':
    main()