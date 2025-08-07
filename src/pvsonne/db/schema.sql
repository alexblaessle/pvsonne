CREATE TABLE data (
    data_id SERIAL PRIMARY KEY,
    Consumption_W integer NOT NULL,
    FullChargeCapacity integer NOT NULL,
    GridFeedIn_W integer NOT NULL,
    Pac_total_W integer NOT NULL,
    Production_W integer NOT NULL,
    RSOC integer NOT NULL,
    SetPoint_W integer NOT NULL,
    Timestamp TIMESTAMP NOT NULL,
    USOC integer NOT NULL,
    UTC_Offet integer NOT NULL,
    ic_status_id integer
);

