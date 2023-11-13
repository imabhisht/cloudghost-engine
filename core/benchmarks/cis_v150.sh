#!/bin/bash
ls
cd ./benchmarks/steampipe-mod-aws-compliance
ls
# steampipe check benchmark.cis_v150 --var 'common_dimensions=["895261382174","aws_aw2413","ap-south-1"]'  --export=output.json
steampipe check benchmark.cis_v150 --var 'common_dimensions=["$1","$2","$1"]'  --export=../output.json