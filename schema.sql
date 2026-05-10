-- Removing existing tables if they already exist
DROP TABLE IF EXISTS shipments;
DROP TABLE IF EXISTS suppliers;

-- Create suppliers table
CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier_name TEXT,
    country TEXT
);

-- Create shipments table
CREATE TABLE shipments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT,
    planned_eta TEXT,
    supplier_id INTEGER,       
    actual_eta TEXT,
    item_code TEXT,
    -- Linking shipments to suppliers table
    FOREIGN KEY (supplier_id)
    REFERENCES suppliers(supplier_id)
);

/*Foreign key: https://www.w3schools.com/sql/sql_foreignkey.asp */