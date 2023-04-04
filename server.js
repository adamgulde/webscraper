import * as promise from "./node_modules/mysql2/promise.js";
            export const insertIntoDB = async (positiveID) => {
                const connection = await promise.createConnection({
                    // not me NOT encrypting my data!??
                    host: "sql9.freesqldatabase.com",
                    user: "sql9609574",
                    password: "U6JqdflMxh",
                    database: "sql9609574",
                    port:3306,
                })
                try {
                    await connection.query(
                        "INSERT INTO distrowebscraper (positiveID) VALUES ("+positiveID+")"
                    );
                    console.log("Inserted ("+positiveID+") into DB")
                } catch (error) {
                    console.log(error)
                }
            };

insertIntoDB(84082862)