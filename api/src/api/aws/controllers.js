const elasticClient = require("../../init/elastic");
const steampipe_query = require("../steampipe/query.json");


module.exports.test = async (req, res) => {
    try {
        await elasticClient.indices.create({ index: "test1" });
        console.log("Index created");
        return res.status(200).json({ message: "AWS Controller Test Route" });
    } catch (error) {
        console.log(error);
        return res.status(500).json({ error: error.message });
    }
}

module.exports.query_aws = async (req,res) => {
    try {
        
        const result = await elasticClient.index({
            index: "posts",
            document: {
              test: "hello"
            },
          });
        
        return res.status(200).json({ message: "Querying AWS" , data: result });
    } catch (error) {
        console.log(error);
        return res.status(500).json({ error: error.message });
    }
}