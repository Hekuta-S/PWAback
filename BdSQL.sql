-- Crear base de datos (si aún no existe)
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = N'PWADatabase')
BEGIN
    CREATE DATABASE PWADatabase;
END
GO

USE PWADatabase;
GO

-- Crear tabla items
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'items')
BEGIN
    CREATE TABLE items (
        id INT IDENTITY(1,1) PRIMARY KEY,
        title NVARCHAR(255) NOT NULL,
        description NVARCHAR(MAX),
        synced BIT DEFAULT 0
    );
END
GO
select * from items