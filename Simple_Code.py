#HackBioInternship: Team Histidine Stage 0 Task

#Task:
# A simple python script for printing the names, slack username, country,
# 1 hobby, affiliations of people on your team and
# and the DNA sequence of the genes they love most.
#Author:Lucia Uchegbu
#GitHub:https://github.com/LuciaUchegbu
#Linkedin: www.linkedin.com/in/luciauchegbu

#Step1 - Stored team Histidine member's information in Tuples

Lucia = (
    "Lucia Uchegbu",  # Name
    "@Lucia",         # Slack Username
    "Nigeria",        # Country
    "Social Media Management",  # Hobby
    "Federal University Oye-Ekiti Nigeria",  # Affiliation
    "TP53 Tumor Protein",  # Favourite Gene
    """TP53 [organism=Homo sapiens] [GeneID=7157] [RefSeq=NM_000546.6] [region=cds]
    ATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCC"""  # DNA Sequence
)

Archana = (
    "Archana Nadig",  # Name
    "@Archana",       # Slack Username
    "India",          # Country
    "Playing Chess",  # Hobby
    "University of York, UK",  # Affiliation
    "Tinman",         # Favourite Gene
    """NT_033777.3:21378977-21381970 Drosophila melanogaster chromosome 3R
    TCAGTACCAAAATCGAGCTGACAAATTGCAGAC"""  # DNA Sequence
)

Sam = (
    "Samuella Ebeny",  # Name
    "@Sam NY",         # Slack Username
    "France",          # Country
    "Reading",         # Hobby
    "Sorbonne University",  # Affiliation
    "SLC9A2",          # Favourite Gene
    """NC_000002.12:102619553-102711355 Homo sapiens chromosome 2, GRCh38.p14 Primary Assembly
    GGAGAGCAGCGCACCGGCATGGGCAGGCGGCCGGCGGC"""  # DNA Sequence
)

Chimbusonma = (
    "Chimbusonma Amaechina",  # Name
    "@Sonma",                 # Slack Username
    "Nigeria",                # Country
    "Reading",                # Hobby
    "Grambling State University, United States",  # Affiliation
    "BRCA1",                  # Favourite Gene
    """NC_000017.11:43044295-43170245 Homo sapiens chromosome 17, GRCh38.p14 Primary Assembly
    ATGGATTTATCTGCTCTTCGGAAAAGCAAGAGGCTGCTGAGGATC"""  # DNA Sequence
)

Antara = (
    "Antara Ghanta",  # Name
    "@Antara",        # Slack Username
    "India",          # Country
    "Reading",        # Hobby
    "Nottingham Trent University, UK",  # Affiliation
    "HMOX1 - Heme Oxygenase 1",  # Favourite Gene
    """NC_000022.11:35381096-35394207 HMOX1 [organism=Homo sapiens] [GeneID=3162] [chromosome=22]
    AACGCCTGCCTCCTCTCGAGCGTCCTCAGCGCAGCCGCCGCCCGC"""  # DNA Sequence
)

Khanh = (
    "Khanh Gia Duong",  # Name
    "@Khanh",           # Slack Username
    "Vietnam",          # Country
    "Watching Movies",  # Hobby
    "Asian University for Women",  # Affiliation
    "BRCA1",            # Favourite Gene
    """NC_000017.11:43044295-43170245 Homo sapiens chromosome 17, GRCh38.p14 Primary Assembly
    ATGGATTTATCTGCTCTTCGGAAAAGCAAGAGGCTGCTGA"""  # DNA Sequence
)

Antsaniony = (
    "Herimampionona Antsaniony",  # Name
    "@Antsaniony",                # Slack Username
    "Madagascar",                 # Country
    "Hiking",                     # Hobby
    "University of Antananarivo", # Affiliation
    "CD79a",                      # Favourite Gene
    """NM_001783.4 Homo sapiens CD79a molecule (CD79A), transcript variant 1, mRNA
    CAAACTAACCAACCCACTGGGAGAAGATGCCTGGGGGTCCAGG"""  # DNA Sequence
)

Saumi = (
    "Saumi Shah",                # Name
    "@Antsaniony",               # Slack Username
    "India",                     # Country
    "Listening to song",         # Hobby
    "SJSU",                      # Affiliation
    "TNF",                       # Favourite Gene
    """>NC_000006.12:31575565-31578336 Homo sapiens chromosome 6, GRCh38.p14 Primary Assembly
AGCAGACGCTCCCTCAGCAAGGACAGCAGAGGACCAGCTAAGAGGGAGAGAAGCAACTACAGA"""  # DNA Sequence
)


Sarah = (
    "Sarah Adeyemi",             # Name
    "@Sarah4God",                # Slack Username
    "USA",                       # Country
    "Reading",                  # Hobby
    "Morgan State University",   # Affiliation
    "TNF",                       # Favourite Gene
    """>NC_000006.12:31575565-31578336 Homo sapiens chromosome 6, GRCh38.p14 Primary Assembly
AGCAGACGCTCCCTCAGCAAGGACAGCAGAGGACCAGCTAAGAGGGAGAGAAGCAACTACAGA"""  # DNA Sequence
)

#Step 2- Print the Data
team = [Lucia, Archana, Sam, Chimbusonma, Antara, Khanh, Antsaniony, Saumi, Sarah]
for member in team:
    print("=" * 60)
    print(f"Name: {member[0]}")
    print(f"Slack Username: {member[1]}")
    print(f"Country: {member[2]}")
    print(f"Hobby: {member[3]}")
    print(f"Affiliation: {member[4]}")
    print(f"Favourite Gene: {member[5]}")
    print("DNA Sequence of Favoured Gene:")
    print(member[6])
    print("=" * 60, "\n")

