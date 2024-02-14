-- converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
ALTER DATABASE hbtn_0c_0
SET CHARSET=utf8mb4, COLLATE=utf8mb4_unicode_ci;
ALTER TABLE first_table
SET CHARSET=utf8mb4, COLLATE=utf8mb4_unicode_ci;
