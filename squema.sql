DROP TABLE IF EXISTS shipments;

CREATE TABLE shipments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT,
    planned_eta TEXT,
    supplier_code TEXT,
    supplier_name TEXT,
    actual_eta TEXT,
    item_code TEXT
);