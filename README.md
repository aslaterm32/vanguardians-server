# Vanguardians Server

## Installing required libraries:

Run the follwing commands within `.`:

```shell
npm init -y
```

```shell
npm install
```

## Setting up the database:

In the `.env` file, set DB_URL to the URL of your chosen PostgreSQL database.

Run the following commands from within `.`:

```shell
npm run setup-db
```

## Running the server:

In the `.env` file, set PORT equal to a port of your choosing.

Run the following commands from within `.`:

```shell
npm run dev
```