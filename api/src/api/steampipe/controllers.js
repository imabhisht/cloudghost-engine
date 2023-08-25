const sequelize = require('../../init/sequalize')();
const Query = require("./query.json");

module.exports.query = async(req, res) => {
    try {
        const { connection_id, query } = req.body;

        if(!Query.hasOwnProperty(query)) {
            return res.status(500).send("Query not found");
        }
        const sql_query = Query[query].replace(/{{connection_id}}/g, connection_id);
        const [results, metadata] = await sequelize.query(sql_query);
        return res.send(results);
    } catch (error) {
        return res.status(500).send(error.message)
    }
}

module.exports.dynamicQuery = async(req, res) => {
    try {
        let { query, variables } = req.body;

        // Loop through the variables object and replace placeholders
        for (const key in variables) {
        const placeholder = `{{${key}}}`;
        const value = variables[key];
        query = query.replace(new RegExp(placeholder, 'g'), value);
        }

        // Now sql_query should have placeholders replaced with actual values
        const [results, metadata] = await sequelize.query(query);

        return res.send(results);
    } catch (error) {
        return res.status(500).send(error.message);
    }
}