-- Sample data for testing and development
-- Run this after creating the schema to populate with sample records

INSERT INTO sample_table (first_name, last_name, date_of_birth) VALUES
('John', 'Smith', '1990-05-15'),
('Jane', 'Doe', '1985-08-22'),
('Michael', 'Johnson', '1992-12-03'),
('Sarah', 'Williams', '1988-03-17'),
('David', 'Brown', '1995-09-08'),
('Emily', 'Davis', '1987-11-25'),
('Christopher', 'Miller', '1991-07-14'),
('Ashley', 'Wilson', '1993-01-30'),
('Matthew', 'Moore', '1989-06-12'),
('Jessica', 'Taylor', '1994-04-28');

-- Bears data
INSERT INTO bears (name, species, age, habitat) VALUES
('Bruno', 'Grizzly Bear', 12, 'North American Forests'),
('Frost', 'Polar Bear', 8, 'Arctic Tundra'),
('Shadow', 'Black Bear', 6, 'Appalachian Mountains'),
('Bamboo', 'Giant Panda', 10, 'Chinese Bamboo Forests'),
('Cinnamon', 'Brown Bear', 15, 'Alaskan Wilderness'),
('Luna', 'Spectacled Bear', 5, 'South American Andes'),
('Midnight', 'Asian Black Bear', 9, 'Himalayan Forests'),
('Honey', 'Sun Bear', 4, 'Southeast Asian Rainforest'),
('Storm', 'Kodiak Bear', 18, 'Kodiak Island Alaska'),
('Maple', 'Kermode Bear', 7, 'British Columbia Rainforest');