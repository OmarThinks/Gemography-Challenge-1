[![CircleCI](https://circleci.com/gh/OmarThinks/Gemography-Challenge-1.svg?style=svg)](https://circleci.com/gh/OmarThinks/Gemography-Challenge-1)
[![CircleCI Build Status](https://circleci.com/gh/OmarThinks/Gemography-Challenge-1.svg?style=shield "CircleCI Build Status")](https://circleci.com/gh/OmarThinks/Gemography-Challenge-1) 
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/OmarThinks/CircleCI-hello-world/master/LICENSE) 


# Gemography-Challenge-1
Submitting a challenge to Gemography




## Challenge Reference:

<a href="https://github.com/gemography/backend-coding-challenge">
Backend Challenge</a>






# 1) RESTful API:

The RESTful API has only one endpoint:

<h2> <a href="http://127.0.0.1:8000/api/search">http://127.0.0.1:8000/api/search</a>:</h2>
The inputs are passed as query parameters:

- **`order`**: `asc` or `desc`
- **`date`**:
	- It has the format of **`YYYY-MM-DD`**
	- Example: `2019-4-25`
- **`records`**:
	- How many repositories do you want to check
	- Min Value : 1
	- Max Value : 1000

## Example:

<b>

```
http://127.0.0.1:8000/api/search?date=2019-04-25&order=desc&records=100
```
</b>


The response will look like:


<b>

```json
{
    "success": true,
    "data": [
        {
            "repos": [
                {
                    "url": "https://github.com/neherlab/covid19_scenarios",
                    "name": "covid19_scenarios",
                    "full_name": "neherlab/covid19_scenarios",
                    "language": "JavaScript"
                },
                {
                    "url": "https://github.com/mandatoryprogrammer/CursedChrome",
                    "name": "CursedChrome",
                    "full_name": "mandatoryprogrammer/CursedChrome",
                    "language": "JavaScript"
                },
                ...
            ],
            "length": 15,
            "language": "JavaScript"
        },
        {
            "repos": [
                {
                    "url": "https://github.com/timothycrosley/portray",
                    "name": "portray",
                    "full_name": "timothycrosley/portray",
                    "language": "Python"
                },
                {
                    "url": "https://github.com/sustrik/uxy",
                    "name": "uxy",
                    "full_name": "sustrik/uxy",
                    "language": "Python"
                },
                ...
            ],
            "length": 14,
            "language": "Python"
        },
        {
            "repos": [
                {
                    "url": "https://github.com/prisma/migrate",
                    "name": "migrate",
                    "full_name": "prisma/migrate",
                    "language": "TypeScript"
                },
                {
                    "url": "https://github.com/coderoad/coderoad-vscode",
                    "name": "coderoad-vscode",
                    "full_name": "coderoad/coderoad-vscode",
                    "language": "TypeScript"
                },
                ...
            ],
            "length": 7,
            "language": "TypeScript"
        },
        ...
    ]
}
```

</b>


## Displaying errors:


<b>

```
http://127.0.0.1:8000/api/search
```
</b>


The response will look like:


<b>

```json
{
	"success":false,
	"data":
	{
		"date":["This field is required."],
		"order":["This field is required."],
		"records":["This field is required."]
	}
}
```

</b>

















