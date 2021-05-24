import sqlite3

connection = sqlite3.connect("HLA-registry.db")
connection.execute('''CREATE TABLE IF NOT EXISTS hla_registry (donor_num INTEGER PRIMARY KEY, 
                    donor_id TEXT, 
                    sex TEXT, 
                    year_of_birth INTEGER, 
                    typing_date TEXT, 
                    kit TEXT, 
                    locus_A TEXT, 
                    locus_B TEXT, 
                    locus_C TEXT, 
                    locus_DRB1 TEXT, 
                    locus_DQB1 TEXT
                    )''')

connection.commit()

with open("C:\\Users\\chera\\Desktop\\Работа\\Регистр_результаты\\Регистр_общая таблица.csv", "r") as registry:
    table_names = registry.readline().strip().split(";")
    for line in registry:
        clean_line = line.strip().split(";")
        for field in range(3, 12):
            if "NEW" in clean_line[field]:
                print(f"new allele in {clean_line[1]}")
            if '-' in clean_line[field]:
                clean_line[field] = clean_line[field - 1]
        donor_num = int(clean_line[1][3:])
        donor_ID = clean_line[1]
        sex = clean_line[12]
        year_of_birth = int(clean_line[13])
        typing_date = clean_line[0]
        kit = clean_line[14]
        locus_A_genotype = clean_line[2][2:] + ',' + clean_line[3][2:]
        locus_B_genotype = clean_line[4][2:] + ',' + clean_line[5][2:]
        locus_C_genotype = clean_line[6][2:] + ',' + clean_line[7][2:]
        locus_DRB1_genotype = clean_line[8][5:] + ',' + clean_line[9][5:]
        locus_DQB1_genotype = clean_line[10][5:] + ',' + clean_line[11][5:]

        query = '''INSERT INTO hla_registry (donor_num, donor_id, sex, year_of_birth, typing_date, kit, locus_A, 
        locus_B, locus_C, locus_DRB1, locus_DQB1) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

        connection.execute(query, [donor_num,
                                   donor_ID,
                                   sex,
                                   year_of_birth,
                                   typing_date,
                                   kit,
                                   locus_A_genotype,
                                   locus_B_genotype,
                                   locus_C_genotype,
                                   locus_DRB1_genotype,
                                   locus_DQB1_genotype])

connection.commit()

# проверить как работает UPDATE

query = '''UPDATE hla_registry 
            SET sex = 1
            WHERE sex = "ж"'''
connection.execute(query)
connection.execute('''UPDATE hla_registry
                        SET sex = 0
                        WHERE sex = "м"''')
connection.commit()

# проверить как работает DELETE
query = '''DELETE from hla_registry
           WHERE year_of_birth > 2000'''
connection.execute(query)
connection.commit()

connection.close()
