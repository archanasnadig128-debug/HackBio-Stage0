# HackBio Internship: Team Histidine - Stage 0
# Task: Print your team information (Name, Slack username, Country, Hobby, Affiliation, and DNA sequence of favourite gene)
# Step 1 - Store each team member's information in a dictionary

# Each key in 'team' represents one member.
# Each member has their own dictionary with labeled fields for clarity.
team = {
    "Archana": {
        "Name": "Archana Nadig",
        "Slack Username": "@Archana",
        "Country": "India",
        "Hobby": "Playing Chess",
        "Affiliation": "University of York, UK",
        "Favoured Gene": "Tinman",
        "DNA Sequence": """NT_033777.3:21378977-21381970 Drosophila melanogaster chromosome 3R
        TCAGTACCAAAATCGAGCTGACAAATTGCAGAC"""
    },
    "Lucia": {
        "Name": "Lucia Uchegbu",
        "Slack Username": "@Lucia",
        "Country": "Nigeria",
        "Hobby": "Social Media Management",
        "Affiliation": "Federal University Oye-Ekiti Nigeria",
        "Favoured Gene": "TP53 Tumor Protein",
        "DNA Sequence": """TP53 [organism=Homo sapiens] [GeneID=7157] [RefSeq=NM_000546.6] [region=cds]
        ATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCC"""
    },
    "Sam": {
        "Name": "Samuella Ebeny",
        "Slack Username": "@Sam NY",
        "Country": "France",
        "Hobby": "Reading",
        "Affiliation": "Sorbonne University",
        "Favoured Gene": "SLC9A2",
        "DNA Sequence": """NC_000002.12:102619553-102711355 Homo sapiens chromosome 2, GRCh38.p14 Primary Assembly
        GGAGAGCAGCGCACCGGCATGGGCAGGCGGCCGGCGGC"""
    },
    "Chimbusonma": {
        "Name": "Chimbusonma Amaechina",
        "Slack Username": "@Sonma",
        "Country": "Nigeria",
        "Hobby": "Reading",
        "Affiliation": "Grambling State University, United States",
        "Favoured Gene": "BRCA1",
        "DNA Sequence": """NC_000017.11:43044295-43170245 Homo sapiens chromosome 17, GRCh38.p14 Primary Assembly
        ATGGATTTATCTGCTCTTCGGAAAAGCAAGAGGCTGCTGAGGATC"""
    },
    "Antara": {
        "Name": "Antara Ghanta",
        "Slack Username": "@Antara",
        "Country": "India",
        "Hobby": "Reading",
        "Affiliation": "Nottingham Trent University, UK",
        "Favoured Gene": "HMOX1 - Heme Oxygenase 1",
        "DNA Sequence": """NC_000022.11:35381096-35394207 HMOX1 [organism=Homo sapiens] [GeneID=3162] [chromosome=22]
        AACGCCTGCCTCCTCTCGAGCGTCCTCAGCGCAGCCGCCGCCCGC"""
    },
    "Khanh": {
        "Name": "Khanh Gia Duong",
        "Slack Username": "@Khanh",
        "Country": "Vietnam",
        "Hobby": "Watching Movies",
        "Affiliation": "Asian University for Women",
        "Favoured Gene": "BRCA1",
        "DNA Sequence": """NC_000017.11:43044295-43170245 Homo sapiens chromosome 17, GRCh38.p14 Primary Assembly
        ATGGATTTATCTGCTCTTCGGAAAAGCAAGAGGCTGCTGA"""
    },
    "Antsaniony": {
        "Name": "Herimampionona Antsaniony",
        "Slack Username": "@Antsaniony",
        "Country": "Madagascar",
        "Hobby": "Hiking",
        "Affiliation": "University of Antananarivo",
        "Favoured Gene": "CD79a",
        "DNA Sequence": """NM_001783.4 Homo sapiens CD79a molecule (CD79A), transcript variant 1, mRNA
        CAAACTAACCAACCCACTGGGAGAAGATGCCTGGGGGTCCAGG"""
    }
}

# Step 2 - Loop through the dictionary and print each team member's information
for member, info in team.items():
    print("=" * 60)  # Print separator line for neat output
    for key, value in info.items():
        # Print each field label (key) and its corresponding data (value)
        print(f"{key}: {value}")
    print("=" * 60, "\n")  # Add a blank line after each member for readability
