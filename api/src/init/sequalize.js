// require('dotenv').config();
const { Sequelize } = require('sequelize');

const sequelize = new Sequelize({
    dialect: 'postgres',
    host: process.env.CG_STEAMPIPE_HOSTNAME,
    port: process.env.CG_STEAMPIPE_PORT,
    database: process.env.CG_STEAMPIPE_DATABASE,
    username: process.env.CG_STEAMPIPE_USERNAME,
    password: process.env.CG_STEAMPIPE_PASSWORD,
});

try {
    sequelize.authenticate();
    console.log('[CloudGhost-API]: Connection has been established successfully.');
} catch (error) {
    console.error('[CloudGhost-API]: Unable to connect to the database:', error);
    throw error;
}

module.exports = sequelize; 

// authenticate sequlize in try-catch before exporting


// module.exports = async() => {
//     try {
//         await sequelize.authenticate();
//         console.log('[CloudGhost-API]: Connection has been established successfully.');
//         return sequelize;
//     } catch (error) {
//         console.error('[CloudGhost-API]: Unable to connect to the database:', error);
//         throw error;
//     }
// }


