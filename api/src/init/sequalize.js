// require('dotenv').config();
const { Sequelize } = require('sequelize');

module.exports = new Sequelize({
    dialect: 'postgres',
    host: process.env.CG_STEAMPIPE_HOSTNAME,
    port: process.env.CG_STEAMPIPE_PORT,
    database: process.env.CG_STEAMPIPE_DATABASE,
    username: process.env.CG_STEAMPIPE_USERNAME,
    password: process.env.CG_STEAMPIPE_PASSWORD,
});

// const initialize = async () => {
//     try {
//         await sequelize.authenticate()
//         console.log('[CloudGhost-API]: Connection has been established successfully.');
//         module.exports = await sequelize; 
//     } catch (error) {
//         console.error('[CloudGhost-API]: Unable to connect to the database:', error);
//         //Print the Configs
//         console.log(process.env.CG_STEAMPIPE_HOSTNAME);
//         console.log(process.env.CG_STEAMPIPE_PORT);
//         console.log(process.env.CG_STEAMPIPE_DATABASE);
//         console.log(process.env.CG_STEAMPIPE_USERNAME);
//         console.log(process.env.CG_STEAMPIPE_PASSWORD);
        
//         throw error;
//     }
// }


