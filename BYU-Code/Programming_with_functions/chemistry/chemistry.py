"""
    Author:  Francisco Javier Zúñiga Sancén

    Class:  CSE111-23s-a3

    Instructor:  Brother Curtis Nelson

    Date:  06/10/2023

    Version:  1.0

"""


from formula import parse_formula

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1


def main():
    # Get a chemical formula for a molecule from the user.

    formula = input("Enter a molecule formula: ")

    # Get the mass of a chemical sample in grams from the user.

    mass_in_grams = float(input("Enter the mass of a chemical sample in grams: "))

    # Call the make_periodic_table function and
    # store the periodic table in a variable.
    make_periodic_table()
    periodic_table_dict = make_periodic_table()

    # Call the parse_formula function to convert the
    # chemical formula given by the user to a compound
    # list that stores element symbols and the quantity
    # of atoms of each element in the molecule.

    formula_list = parse_formula(formula, periodic_table_dict)
    print(formula_list)


    compute_molar_mass(periodic_table_dict, formula_list, mass_in_grams)

def make_periodic_table():

    periodic_table_dict = {
        #ymbol:	[name,	atomic_mass     ],
    "Ac" : ["Actinium", 227],
    "Ag" : ["Silver", 107.8682],
    "Al" : ["Aluminum", 26.9815386],
    "Ar" : ["Argon", 39.948],
    "As" : ["Arsenic", 74.9216],
    "At" : ["Astatine", 210],
    "Au" : ["Gold", 196.966569],
    "B" :  ["Boron", 10.811],
    "Ba" : ["Barium", 137.327],
    "Be" : ["Beryllium", 9.012182],
    "Bi" : ["Bismuth", 208.9804],
    "Br" : ["Bromine", 79.904],
    "C" : ["Carbon", 12.0107],
    "Ca" : ["Calcium", 40.078],
    "Cd" : ["Cadmium", 112.411],
    "Ce" : ["Cerium", 140.116],
    "Cl" : ["Chlorine", 35.453],
    "Co" : ["Cobalt", 58.933195],
    "Cr" : ["Chromium", 51.9961],
    "Cs" : ["Cesium", 132.9054519],
    "Cu" : ["Copper", 63.546],
    "Dy" : ["Dysprosium",162.5],
    "Er" : ["Erbium",167.259],
    "Eu" : ["Europium",151.964],
    "F" : ["Fluorine",18.9984032],
    "Fe" : ["Iron",55.845],
    "Fr" : ["Francium", 223],
    "Ga" : ["Gallium", 69.723],
    "Gd" : ["Gadolinium", 157.25],
    "Ge" : ["Germanium", 72.64],
    "H" : ["Hydrogen", 1.00794],
    "He" : ["Helium", 4.002602],
    "Hf" : ["Hafnium", 178.49],
    "Hg" : ["Mercury", 200.59],
    "Ho" : ["Holmium", 164.93032],
    "I" : ["Iodine", 126.90447],
    "In" : ["Indium", 114.818],
    "Ir" : ["Iridium", 192.217],
    "K" : ["Potassium", 39.0983],
    "Kr" : ["Krypton", 83.798],
    "La" : ["Lanthanum",	138.90547],
    "Li" : ["Lithium",	6.941],
    "Lu" : ["Lutetium",	174.9668],
    "Mg" : ["Magnesium",	24.305],
    "Mn" : ["Manganese",	54.938045],
    "Mo" : ["Molybdenum",	95.96],
    "N" : ["Nitrogen",	14.0067],
    "Na" : ["Sodium",	22.98976928],
    "Nb" : ["Niobium",	92.90638],
    "Nd" : ["Neodymium",	144.242],
    "Ne" : ["Neon",	20.1797],
    "Ni" : ["Nickel",	58.6934],
    "Np" : ["Neptunium",	237],
    "O" : ["Oxygen",	15.9994],
    "Os" : ["Osmium",	190.23],
    "P" : ["Phosphorus",	30.973762],
    "Pa" : ["Protactinium",	231.03588],
    "Pb" : ["Lead",	207.2],
    "Pd" : ["Palladium",	106.42],
    "Pm" : ["Promethium",	145],
    "Po" : ["Polonium",	209],
    "Pr" : ["Praseodymium",	140.90765],
    "Pt" : ["Platinum",	195.084],
    "Pu" : ["Plutonium",	244],
    "Ra" : ["Radium",	226],
    "Rb" : ["Rubidium",	85.4678],
    "Re" : ["Rhenium",	186.207],
    "Rh" : ["Rhodium",	102.9055],
    "Rn" : ["Radon",	222],
    "Ru" : ["Ruthenium",	101.07],
    "S" : ["Sulfur",	32.065],
    "Sb" : ["Antimony",	121.76],
    "Sc" : ["Scandium",	44.955912],
    "Se" : ["Selenium",	78.96],
    "Si" : ["Silicon",	28.0855],
    "Sm" : ["Samarium",	150.36],
    "Sn" : ["Tin",	118.71],
    "Sr" : ["Strontium",	87.62],
    "Ta" : ["Tantalum",	180.94788],
    "Tb" : ["Terbium",	158.92535],
    "Tc" : ["Technetium",	98],
    "Te" : ["Tellurium",	127.6],
    "Th" : ["Thorium", 232.03806],
    "Ti" : ["Titanium", 47.867],
    "Tl" : ["Thallium", 204.3833],
    "Tm" : ["Thulium", 168.93421],
    "U" : ["Uranium", 238.02891],
    "V" : ["Vanadium", 50.9415],
    "W" : ["Tungsten", 183.84],
    "Xe" : ["Xenon", 131.293],
    "Y" : ["Yttrium", 88.90585],
    "Yb" : ["Ytterbium", 173.054],
    "Zn" : ["Zinc",	65.38],
    "Zr" : ["Zirconium", 91.224],

    }

    return periodic_table_dict

def compute_molar_mass(periodic_table_dict, formula_list, mass_in_grams):
    mol_mass_of_glocose = 0

    for key, value in periodic_table_dict.items():
        name = value[NAME_INDEX]
        at_mass = value[ATOMIC_MASS_INDEX]
        #print(f"name = {name}, atomic mass = {at_mass}")

    for item in formula_list:
        elem_key = item[0]
        num_of_atoms = item[1]
        elem_list = periodic_table_dict[elem_key]
        elem_name = elem_list[NAME_INDEX]
        atom_mass = elem_list[ATOMIC_MASS_INDEX]


    # Call the compute_molar_mass function to compute the
    # molar mass of the molecule from the compound list.
    # Compute the number of moles in the sample.
    # Print the molar mass.
    # Print the number of moles.
    #Print the name and atomic mass for each chemical element on a separate line. Do not print the chemical element symbols.

        print()
        atomic_mass = num_of_atoms * atom_mass
        mol_mass_of_glocose += atomic_mass
        print(f"{elem_name} | has {num_of_atoms} atoms | atom element mass {atom_mass} |\n total atom mass for this element in the molecule {atomic_mass} ")
    num_of_moles = mass_in_grams / mol_mass_of_glocose
    print()
    print(f"This molecule a molar mass of glucose of: {mol_mass_of_glocose} grams/mole")
    print()
    print(f"The number of moles in this molecule is: {num_of_moles} moles ")


    pass


if __name__ == "__main__":
    main()
