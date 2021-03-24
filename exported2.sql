--
-- File generated with SQLiteStudio v3.3.2 on Thu Mar 18 16:12:30 2021
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: ChemicalHazards
DROP TABLE IF EXISTS ChemicalHazards;

CREATE TABLE ChemicalHazards (
    id          INTEGER PRIMARY KEY ASC AUTOINCREMENT
                        NOT NULL,
    Chemical    STRING  NOT NULL,
    Flammable   BOOLEAN DEFAULT (false) 
                        NOT NULL,
    Corrosive   BOOLEAN DEFAULT (FALSE) 
                        NOT NULL,
    Toxic       BOOLEAN DEFAULT (false) 
                        NOT NULL,
    Environment BOOLEAN DEFAULT (false) 
                        NOT NULL,
    Hazardous   BOOLEAN DEFAULT (false) 
                        NOT NULL,
    Respiratory BOOLEAN DEFAULT (false) 
                        NOT NULL,
    HHM         BOOLEAN DEFAULT (false) 
                        NOT NULL
);

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                1,
                                'Phosphoric Acid',
                                'FALSE',
                                'TRUE',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'FALSE'
                            );

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                2,
                                'Acetonitrile',
                                'TRUE',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'FALSE'
                            );

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                3,
                                'Benzy Alcohol',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'TRUE',
                                'FALSE',
                                'FALSE'
                            );

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                4,
                                'EDTA',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'TRUE',
                                'FALSE',
                                'FALSE'
                            );

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                5,
                                'Sodium Hydroxide',
                                'FALSE',
                                'TRUE',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'FALSE'
                            );

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                6,
                                'Ammonium Acetate',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'TRUE',
                                'FALSE',
                                'FALSE'
                            );

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                7,
                                'Ammonium Hydroxide',
                                'FALSE',
                                'TRUE',
                                'FALSE',
                                'FALSE',
                                'TRUE',
                                'FALSE',
                                'FALSE'
                            );

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                8,
                                'Acetone',
                                'TRUE',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'TRUE',
                                'TRUE',
                                'FALSE'
                            );

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                9,
                                'DMSO',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'TRUE',
                                'FALSE',
                                'FALSE'
                            );

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                10,
                                'Guanidine',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'TRUE',
                                'FALSE',
                                'FALSE'
                            );

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                11,
                                'Methanol',
                                'TRUE',
                                'FALSE',
                                'TRUE',
                                'FALSE',
                                'TRUE',
                                'FALSE',
                                'FALSE'
                            );

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                12,
                                'Ammonium Formate',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'TRUE',
                                'FALSE',
                                'FALSE'
                            );

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                13,
                                'Formic Acid',
                                'TRUE',
                                'TRUE',
                                'TRUE',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'FALSE'
                            );

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                14,
                                'Ethylmaleidmide',
                                'FALSE',
                                'TRUE',
                                'TRUE',
                                'FALSE',
                                'TRUE',
                                'FALSE',
                                'FALSE'
                            );

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                15,
                                'Azide',
                                'FALSE',
                                'FALSE',
                                'TRUE',
                                'TRUE',
                                'FALSE',
                                'FALSE',
                                'TRUE'
                            );

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                16,
                                'Sodium Sulfate',
                                'FALSE',
                                'TRUE',
                                'FALSE',
                                'FALSE',
                                'TRUE',
                                'FALSE',
                                'FALSE'
                            );

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                17,
                                'Sodium Dodecyl Sulfate',
                                'TRUE',
                                'TRUE',
                                'FALSE',
                                'FALSE',
                                'TRUE',
                                'FALSE',
                                'FALSE'
                            );

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                18,
                                'Urea',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'TRUE',
                                'FALSE',
                                'FALSE'
                            );

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                19,
                                'Tris',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'TRUE',
                                'FALSE',
                                'FALSE'
                            );

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                20,
                                'Ethanol',
                                'TRUE',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'FALSE'
                            );

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                21,
                                'Sodium Cyanoborohydride',
                                'TRUE',
                                'TRUE',
                                'TRUE',
                                'TRUE',
                                'FALSE',
                                'FALSE',
                                'TRUE'
                            );

INSERT INTO ChemicalHazards (
                                id,
                                Chemical,
                                Flammable,
                                Corrosive,
                                Toxic,
                                Environment,
                                Hazardous,
                                Respiratory,
                                HHM
                            )
                            VALUES (
                                22,
                                'Sodium Perchlorate',
                                'TRUE',
                                'FALSE',
                                'FALSE',
                                'FALSE',
                                'TRUE',
                                'FALSE',
                                'TRUE'
                            );


-- Table: Replacements
DROP TABLE IF EXISTS Replacements;

CREATE TABLE Replacements (
    OldName         STRING PRIMARY KEY
                           UNIQUE,
    CorrectSpelling STRING
);

INSERT INTO Replacements (
                             OldName,
                             CorrectSpelling
                         )
                         VALUES (
                             'NaOH',
                             'Sodium Hydroxide'
                         );

INSERT INTO Replacements (
                             OldName,
                             CorrectSpelling
                         )
                         VALUES (
                             'NaCl',
                             'Sodium Chloride'
                         );

INSERT INTO Replacements (
                             OldName,
                             CorrectSpelling
                         )
                         VALUES (
                             'PS20',
                             'Polysorbate 20'
                         );

INSERT INTO Replacements (
                             OldName,
                             CorrectSpelling
                         )
                         VALUES (
                             'PS80',
                             'Polysorbate 80'
                         );

INSERT INTO Replacements (
                             OldName,
                             CorrectSpelling
                         )
                         VALUES (
                             'CHAPS',
                             '3-((3-cholamidopropyl) dimethylammonio)-1-propanesulfonate(CHAPS)'
                         );

INSERT INTO Replacements (
                             OldName,
                             CorrectSpelling
                         )
                         VALUES (
                             'IGF-1',
                             'Insulin Growth Factor - 1'
                         );

INSERT INTO Replacements (
                             OldName,
                             CorrectSpelling
                         )
                         VALUES (
                             'DTPA',
                             'Diethylenetriamine Pentaacetate(DTPA)'
                         );

INSERT INTO Replacements (
                             OldName,
                             CorrectSpelling
                         )
                         VALUES (
                             'SDS',
                             'Sodium Dodecyl Sulfate'
                         );

INSERT INTO Replacements (
                             OldName,
                             CorrectSpelling
                         )
                         VALUES (
                             'HFIP',
                             'Hexafluoroisopropanol(HFIP)'
                         );

INSERT INTO Replacements (
                             OldName,
                             CorrectSpelling
                         )
                         VALUES (
                             'HPMC',
                             'Hydroxymethylcellulose'
                         );

INSERT INTO Replacements (
                             OldName,
                             CorrectSpelling
                         )
                         VALUES (
                             'HPBCD',
                             '2-Hydroxypropyl-beta-cyclodextrin'
                         );

INSERT INTO Replacements (
                             OldName,
                             CorrectSpelling
                         )
                         VALUES (
                             'EDTA',
                             'Ethylenediaminetetraacetic acid(EDTA)'
                         );

INSERT INTO Replacements (
                             OldName,
                             CorrectSpelling
                         )
                         VALUES (
                             'EGTA',
                             'ethylene glycol-bis(''-aminoethyl ether)-N, N, N'',N''-tetraacetic acid(EGTA)'
                         );

INSERT INTO Replacements (
                             OldName,
                             CorrectSpelling
                         )
                         VALUES (
                             'Tris',
                             'tris(hydroxymethyl)aminomethane(Tris)'
                         );

INSERT INTO Replacements (
                             OldName,
                             CorrectSpelling
                         )
                         VALUES (
                             'MES',
                             '2-(N-morpholino)ethanesulfonic acid(MES)'
                         );

INSERT INTO Replacements (
                             OldName,
                             CorrectSpelling
                         )
                         VALUES (
                             'MOPS',
                             '3-morpholinopropane-1-sulfonic acid(MOPS)'
                         );

INSERT INTO Replacements (
                             OldName,
                             CorrectSpelling
                         )
                         VALUES (
                             'HEPES',
                             '2-[4-(2-hydroxyethyl)piperazin-1-yl]ethanesulfonic acid(HEPES)'
                         );

INSERT INTO Replacements (
                             OldName,
                             CorrectSpelling
                         )
                         VALUES (
                             'HCl',
                             'Hydrochloric Acid'
                         );

INSERT INTO Replacements (
                             OldName,
                             CorrectSpelling
                         )
                         VALUES (
                             'H2O',
                             'Dihydrogen Monoxide(H2O)'
                         );

INSERT INTO Replacements (
                             OldName,
                             CorrectSpelling
                         )
                         VALUES (
                             NULL,
                             NULL
                         );

INSERT INTO Replacements (
                             OldName,
                             CorrectSpelling
                         )
                         VALUES (
                             NULL,
                             NULL
                         );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
