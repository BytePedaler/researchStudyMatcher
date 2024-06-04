"""
I would like to make a program that makes my job easier.
I currently work as a clinical research coordinator in
ophthalmology and we have a few new studies that we have
started working on. I'd like to make a program that a series
of questions about patient data and then prints that data
back to the user and matches them to one of the studies
OR states why they met exclusion criteria.
"""

# Take refraction as input
sphere_power = float(input("Enter the sphere power (include negative sign, if applicable): "))
cylinder_power = float(input("Enter the cylinder power (include negative sign, if applicable): "))
axis_degrees = int(input("Enter the axis in degrees: "))

# If input is in plus-cylinder, convert to minus-cylinder.
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
print("This patient's converted refraction is: " +
      "S:" + str(sph_pow_neg_cyl) + "  " +
      "C:" + str(neg_cyl_pow) + "  " +
      "A:" + str(neg_cyl_axis_deg))

# If cylinder is less than -1.00: Convert refraction to spherical equivalent
# Conversion is: SE = (S + (C/2))
if neg_cyl_pow >= -1.00 and neg_cyl_pow <= 0.00:
    # Should I pass this into its own function?
    # cyl_pow_conv = cylinder_power
    spherical_equivalent = (sphere_power + (neg_cyl_pow/2))
    # BUG: this seems to print regardless of the if statement, not sure why
    print("This patient's spherical equivalent is: " + str(spherical_equivalent))
else:
    print("This patient should not have a spherical equivalent.")

# Determine myopic or not

    # If yes: Diagnosis of glaucoma or not?

        # If yes: Questions about Cohort 2

        # if no: Questions about Cohort 1

    # If no: Verify axial length:

        # If axial length is greater than 26: Question about glaucoma -> follow the question set above

        # If axial length is less than 26: Questions about Cohort 3


def main():
    pass

if __name__ == '__main__':
    main()