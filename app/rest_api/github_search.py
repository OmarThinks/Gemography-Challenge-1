from .serializers import (GithubSearchRepoSerializer, build_queries)
import requests
import json

"""

dummy_data = {
	"data": [
		{
			"full_name": "FoldingAtHome/coronavirus",
			"language": "Python",
			"name": "coronavirus",
			"url": "https://github.com/FoldingAtHome/coronavirus"
		},
		{
			"full_name": "platinum-engineering/qdao-smartcontract-qdao-locker",
			"language": "JavaScript",
			"name": "qdao-smartcontract-qdao-locker",
			"url": "https://github.com/platinum-engineering/qdao-smartcontract-qdao-locker"
		},
		{
			"full_name": "gaearon/suspense-experimental-github-demo",
			"language": "JavaScript",
			"name": "suspense-experimental-github-demo",
			"url": "https://github.com/gaearon/suspense-experimental-github-demo"
		},
		{
			"full_name": "snowpackjs/create-snowpack-app",
			"language": "JavaScript",
			"name": "create-snowpack-app",
			"url": "https://github.com/snowpackjs/create-snowpack-app"
		},
		{
			"full_name": "sustrik/uxy",
			"language": "Python",
			"name": "uxy",
			"url": "https://github.com/sustrik/uxy"
		},
		{
			"full_name": "bhlvoong/LBTATools",
			"language": "Swift",
			"name": "LBTATools",
			"url": "https://github.com/bhlvoong/LBTATools"
		},
		{
			"full_name": "llSourcell/Programming_Interview_Study_Plan",
			"language": None,
			"name": "Programming_Interview_Study_Plan",
			"url": "https://github.com/llSourcell/Programming_Interview_Study_Plan"
		},
		{
			"full_name": "homeferences/list",
			"language": "JavaScript",
			"name": "list",
			"url": "https://github.com/homeferences/list"
		},
		{
			"full_name": "rasbt/stat479-machine-learning-fs19",
			"language": "Jupyter Notebook",
			"name": "stat479-machine-learning-fs19",
			"url": "https://github.com/rasbt/stat479-machine-learning-fs19"
		},
		{
			"full_name": "ChrisCavs/bounds.js",
			"language": "JavaScript",
			"name": "bounds.js",
			"url": "https://github.com/ChrisCavs/bounds.js"
		},
		{
			"full_name": "IntrinsicLabs/osgood",
			"language": "Rust",
			"name": "osgood",
			"url": "https://github.com/IntrinsicLabs/osgood"
		},
		{
			"full_name": "irsdl/top10webseclist",
			"language": None,
			"name": "top10webseclist",
			"url": "https://github.com/irsdl/top10webseclist"
		},
		{
			"full_name": "tangzixiang0304/Shielded_detector",
			"language": "Python",
			"name": "Shielded_detector",
			"url": "https://github.com/tangzixiang0304/Shielded_detector"
		},
		{
			"full_name": "ZieIony/GuideToCustomViews",
			"language": "Kotlin",
			"name": "GuideToCustomViews",
			"url": "https://github.com/ZieIony/GuideToCustomViews"
		},
		{
			"full_name": "feelschaotic/SDKHotFix",
			"language": "Kotlin",
			"name": "SDKHotFix",
			"url": "https://github.com/feelschaotic/SDKHotFix"
		},
		{
			"full_name": "chris104957/maildown",
			"language": "Python",
			"name": "maildown",
			"url": "https://github.com/chris104957/maildown"
		},
		{
			"full_name": "scastiel/3d-book-image-css-generator",
			"language": "TypeScript",
			"name": "3d-book-image-css-generator",
			"url": "https://github.com/scastiel/3d-book-image-css-generator"
		},
		{
			"full_name": "jiayiliujiayi/2020nCov_individual_archives",
			"language": "R",
			"name": "2020nCov_individual_archives",
			"url": "https://github.com/jiayiliujiayi/2020nCov_individual_archives"
		},
		{
			"full_name": "anandabits/SwiftUI-Processing",
			"language": "Swift",
			"name": "SwiftUI-Processing",
			"url": "https://github.com/anandabits/SwiftUI-Processing"
		},
		{
			"full_name": "luciopaiva/heapify",
			"language": "JavaScript",
			"name": "heapify",
			"url": "https://github.com/luciopaiva/heapify"
		},
		{
			"full_name": "Siderite/LInQer",
			"language": "JavaScript",
			"name": "LInQer",
			"url": "https://github.com/Siderite/LInQer"
		},
		{
			"full_name": "react-navigation/navigation-ex",
			"language": "TypeScript",
			"name": "navigation-ex",
			"url": "https://github.com/react-navigation/navigation-ex"
		},
		{
			"full_name": "smashtestio/smashtest",
			"language": "JavaScript",
			"name": "smashtest",
			"url": "https://github.com/smashtestio/smashtest"
		},
		{
			"full_name": "rasbt/stat453-deep-learning-ss20",
			"language": "Jupyter Notebook",
			"name": "stat453-deep-learning-ss20",
			"url": "https://github.com/rasbt/stat453-deep-learning-ss20"
		},
		{
			"full_name": "AppleIntelWifi/adapter",
			"language": "C",
			"name": "adapter",
			"url": "https://github.com/AppleIntelWifi/adapter"
		},
		{
			"full_name": "chuabingquan/helm",
			"language": "Dart",
			"name": "helm",
			"url": "https://github.com/chuabingquan/helm"
		},
		{
			"full_name": "pvdz/tenko",
			"language": "JavaScript",
			"name": "tenko",
			"url": "https://github.com/pvdz/tenko"
		},
		{
			"full_name": "MaslowCommunityGarden/DUE-Shield",
			"language": None,
			"name": "DUE-Shield",
			"url": "https://github.com/MaslowCommunityGarden/DUE-Shield"
		},
		{
			"full_name": "Jarred-Sumner/git-peek",
			"language": "JavaScript",
			"name": "git-peek",
			"url": "https://github.com/Jarred-Sumner/git-peek"
		},
		{
			"full_name": "twostraws/Brisk",
			"language": "Swift",
			"name": "Brisk",
			"url": "https://github.com/twostraws/Brisk"
		},
		{
			"full_name": "colearninglounge/co-learning-lounge",
			"language": "Jupyter Notebook",
			"name": "co-learning-lounge",
			"url": "https://github.com/colearninglounge/co-learning-lounge"
		},
		{
			"full_name": "ceejbot/economics-of-package-management",
			"language": None,
			"name": "economics-of-package-management",
			"url": "https://github.com/ceejbot/economics-of-package-management"
		},
		{
			"full_name": "MaslowCommunityGarden/3-Bit-CNC-Starter-Pack",
			"language": None,
			"name": "3-Bit-CNC-Starter-Pack",
			"url": "https://github.com/MaslowCommunityGarden/3-Bit-CNC-Starter-Pack"
		},
		{
			"full_name": "fterh/heimdall",
			"language": "TypeScript",
			"name": "heimdall",
			"url": "https://github.com/fterh/heimdall"
		},
		{
			"full_name": "pcomputo/Whole-Foods-Delivery-Slot",
			"language": "Python",
			"name": "Whole-Foods-Delivery-Slot",
			"url": "https://github.com/pcomputo/Whole-Foods-Delivery-Slot"
		},
		{
			"full_name": "Yonghongwei/Gradient-Centralization",
			"language": "Python",
			"name": "Gradient-Centralization",
			"url": "https://github.com/Yonghongwei/Gradient-Centralization"
		},
		{
			"full_name": "fastai/swiftai",
			"language": "Jupyter Notebook",
			"name": "swiftai",
			"url": "https://github.com/fastai/swiftai"
		},
		{
			"full_name": "JSsnippets/JavaScript-snippets",
			"language": None,
			"name": "JavaScript-snippets",
			"url": "https://github.com/JSsnippets/JavaScript-snippets"
		},
		{
			"full_name": "mikelxc/Workarounds-for-ARM-mac",
			"language": None,
			"name": "Workarounds-for-ARM-mac",
			"url": "https://github.com/mikelxc/Workarounds-for-ARM-mac"
		},
		{
			"full_name": "MaslowCommunityGarden/Complete-Ring-Kit",
			"language": None,
			"name": "Complete-Ring-Kit",
			"url": "https://github.com/MaslowCommunityGarden/Complete-Ring-Kit"
		},
		{
			"full_name": "Seb-C/kiss-orm",
			"language": "TypeScript",
			"name": "kiss-orm",
			"url": "https://github.com/Seb-C/kiss-orm"
		},
		{
			"full_name": "jncraton/box-line-text",
			"language": "HTML",
			"name": "box-line-text",
			"url": "https://github.com/jncraton/box-line-text"
		},
		{
			"full_name": "adamwathan/workcation",
			"language": "Vue",
			"name": "workcation",
			"url": "https://github.com/adamwathan/workcation"
		},
		{
			"full_name": "pakastin/car",
			"language": "JavaScript",
			"name": "car",
			"url": "https://github.com/pakastin/car"
		},
		{
			"full_name": "thma/WhyHaskellMatters",
			"language": "Haskell",
			"name": "WhyHaskellMatters",
			"url": "https://github.com/thma/WhyHaskellMatters"
		},
		{
			"full_name": "statebox/awesome-applied-ct",
			"language": None,
			"name": "awesome-applied-ct",
			"url": "https://github.com/statebox/awesome-applied-ct"
		},
		{
			"full_name": "MaslowCommunityGarden/Z-Axis-Kit",
			"language": None,
			"name": "Z-Axis-Kit",
			"url": "https://github.com/MaslowCommunityGarden/Z-Axis-Kit"
		},
		{
			"full_name": "flore2003/staythefuckhome",
			"language": "HTML",
			"name": "staythefuckhome",
			"url": "https://github.com/flore2003/staythefuckhome"
		},
		{
			"full_name": "kethinov/no-cli-ads",
			"language": "JavaScript",
			"name": "no-cli-ads",
			"url": "https://github.com/kethinov/no-cli-ads"
		},
		{
			"full_name": "carbonblack/binee",
			"language": "Go",
			"name": "binee",
			"url": "https://github.com/carbonblack/binee"
		},
		{
			"full_name": "hlldz/dazzleUP",
			"language": "C++",
			"name": "dazzleUP",
			"url": "https://github.com/hlldz/dazzleUP"
		},
		{
			"full_name": "wuhan2020/WebApp",
			"language": "TypeScript",
			"name": "WebApp",
			"url": "https://github.com/wuhan2020/WebApp"
		},
		{
			"full_name": "palewire/nrol-39-logo",
			"language": None,
			"name": "nrol-39-logo",
			"url": "https://github.com/palewire/nrol-39-logo"
		},
		{
			"full_name": "oslabs-beta/Kafka-Sprout",
			"language": "Java",
			"name": "Kafka-Sprout",
			"url": "https://github.com/oslabs-beta/Kafka-Sprout"
		},
		{
			"full_name": "vitechliu/zhuoyao_radar",
			"language": "JavaScript",
			"name": "zhuoyao_radar",
			"url": "https://github.com/vitechliu/zhuoyao_radar"
		},
		{
			"full_name": "JE2Se/AssetScan",
			"language": "Python",
			"name": "AssetScan",
			"url": "https://github.com/JE2Se/AssetScan"
		},
		{
			"full_name": "implus/GFocal",
			"language": "Python",
			"name": "GFocal",
			"url": "https://github.com/implus/GFocal"
		},
		{
			"full_name": "tj/triage",
			"language": "Go",
			"name": "triage",
			"url": "https://github.com/tj/triage"
		},
		{
			"full_name": "zcor/githubjobs",
			"language": None,
			"name": "githubjobs",
			"url": "https://github.com/zcor/githubjobs"
		},
		{
			"full_name": "oslabs-beta/GraphQuill",
			"language": "TypeScript",
			"name": "GraphQuill",
			"url": "https://github.com/oslabs-beta/GraphQuill"
		},
		{
			"full_name": "ookamiinc/kinto",
			"language": None,
			"name": "kinto",
			"url": "https://github.com/ookamiinc/kinto"
		},
		{
			"full_name": "babylonhealth/orbit-mvi",
			"language": "Kotlin",
			"name": "orbit-mvi",
			"url": "https://github.com/babylonhealth/orbit-mvi"
		},
		{
			"full_name": "Shpota/skmz",
			"language": "Go",
			"name": "skmz",
			"url": "https://github.com/Shpota/skmz"
		},
		{
			"full_name": "ricokahler/color2k",
			"language": "TypeScript",
			"name": "color2k",
			"url": "https://github.com/ricokahler/color2k"
		},
		{
			"full_name": "zhihu-huawei251/zhihu-huawei251",
			"language": "HTML",
			"name": "zhihu-huawei251",
			"url": "https://github.com/zhihu-huawei251/zhihu-huawei251"
		},
		{
			"full_name": "covidatlas/coronadatascraper",
			"language": "HTML",
			"name": "coronadatascraper",
			"url": "https://github.com/covidatlas/coronadatascraper"
		},
		{
			"full_name": "qit-team/snow",
			"language": "Go",
			"name": "snow",
			"url": "https://github.com/qit-team/snow"
		},
		{
			"full_name": "codemotionapps/react-native-dark-mode",
			"language": "TypeScript",
			"name": "react-native-dark-mode",
			"url": "https://github.com/codemotionapps/react-native-dark-mode"
		},
		{
			"full_name": "JFreegman/SpicyPass",
			"language": "C++",
			"name": "SpicyPass",
			"url": "https://github.com/JFreegman/SpicyPass"
		},
		{
			"full_name": "synestematic/kord",
			"language": "Python",
			"name": "kord",
			"url": "https://github.com/synestematic/kord"
		},
		{
			"full_name": "zenghongtu/vscode-asciiflow2",
			"language": "JavaScript",
			"name": "vscode-asciiflow2",
			"url": "https://github.com/zenghongtu/vscode-asciiflow2"
		},
		{
			"full_name": "LAB-MI/attestation-deplacement-derogatoire-q4-2020",
			"language": "JavaScript",
			"name": "attestation-deplacement-derogatoire-q4-2020",
			"url": "https://github.com/LAB-MI/attestation-deplacement-derogatoire-q4-2020"
		},
		{
			"full_name": "SforAiDl/genrl",
			"language": "Python",
			"name": "genrl",
			"url": "https://github.com/SforAiDl/genrl"
		},
		{
			"full_name": "taokong/FoveaBox",
			"language": "Python",
			"name": "FoveaBox",
			"url": "https://github.com/taokong/FoveaBox"
		},
		{
			"full_name": "nunomaduro/pest",
			"language": None,
			"name": "pest",
			"url": "https://github.com/nunomaduro/pest"
		},
		{
			"full_name": "oslabs-beta/protographql",
			"language": "JavaScript",
			"name": "protographql",
			"url": "https://github.com/oslabs-beta/protographql"
		},
		{
			"full_name": "Philip-Bachman/amdim-public",
			"language": "Python",
			"name": "amdim-public",
			"url": "https://github.com/Philip-Bachman/amdim-public"
		},
		{
			"full_name": "instillai/Generative-Adversarial-Networks-Roadmap",
			"language": "Python",
			"name": "Generative-Adversarial-Networks-Roadmap",
			"url": "https://github.com/instillai/Generative-Adversarial-Networks-Roadmap"
		},
		{
			"full_name": "open-coronavirus/open-coronavirus",
			"language": "JavaScript",
			"name": "open-coronavirus",
			"url": "https://github.com/open-coronavirus/open-coronavirus"
		},
		{
			"full_name": "uknowsec/SharpToolsAggressor",
			"language": None,
			"name": "SharpToolsAggressor",
			"url": "https://github.com/uknowsec/SharpToolsAggressor"
		},
		{
			"full_name": "zesage/flutter_compass",
			"language": "Dart",
			"name": "flutter_compass",
			"url": "https://github.com/zesage/flutter_compass"
		},
		{
			"full_name": "ErickWendel/ew-ubuntu-setup",
			"language": "Shell",
			"name": "ew-ubuntu-setup",
			"url": "https://github.com/ErickWendel/ew-ubuntu-setup"
		},
		{
			"full_name": "insight-chain/inb-go",
			"language": "Go",
			"name": "inb-go",
			"url": "https://github.com/insight-chain/inb-go"
		},
		{
			"full_name": "google/kf",
			"language": "Python",
			"name": "kf",
			"url": "https://github.com/google/kf"
		},
		{
			"full_name": "xytoki/TCShare",
			"language": "PHP",
			"name": "TCShare",
			"url": "https://github.com/xytoki/TCShare"
		},
		{
			"full_name": "kudelskisecurity/chainoffools",
			"language": "Python",
			"name": "chainoffools",
			"url": "https://github.com/kudelskisecurity/chainoffools"
		},
		{
			"full_name": "hobochild/sandy",
			"language": "Go",
			"name": "sandy",
			"url": "https://github.com/hobochild/sandy"
		},
		{
			"full_name": "karpathy/covid-sanity",
			"language": "Python",
			"name": "covid-sanity",
			"url": "https://github.com/karpathy/covid-sanity"
		},
		{
			"full_name": "sq5bpf/etherify",
			"language": "Shell",
			"name": "etherify",
			"url": "https://github.com/sq5bpf/etherify"
		},
		{
			"full_name": "richardartoul/molecule",
			"language": "Go",
			"name": "molecule",
			"url": "https://github.com/richardartoul/molecule"
		},
		{
			"full_name": "nunomaduro/laravel-mojito",
			"language": "PHP",
			"name": "laravel-mojito",
			"url": "https://github.com/nunomaduro/laravel-mojito"
		},
		{
			"full_name": "midou-tech/articles",
			"language": None,
			"name": "articles",
			"url": "https://github.com/midou-tech/articles"
		},
		{
			"full_name": "Megvii-CSG/MegReader",
			"language": "Python",
			"name": "MegReader",
			"url": "https://github.com/Megvii-CSG/MegReader"
		},
		{
			"full_name": "dair-ai/nlp_fundamentals",
			"language": "Jupyter Notebook",
			"name": "nlp_fundamentals",
			"url": "https://github.com/dair-ai/nlp_fundamentals"
		},
		{
			"full_name": "CyberZHG/keras-radam",
			"language": "Python",
			"name": "keras-radam",
			"url": "https://github.com/CyberZHG/keras-radam"
		},
		{
			"full_name": "fjb040911/Comb",
			"language": "JavaScript",
			"name": "Comb",
			"url": "https://github.com/fjb040911/Comb"
		},
		{
			"full_name": "dfranx/ShaderDebugger",
			"language": "C++",
			"name": "ShaderDebugger",
			"url": "https://github.com/dfranx/ShaderDebugger"
		},
		{
			"full_name": "ryanmcgrath/alchemy",
			"language": "Rust",
			"name": "alchemy",
			"url": "https://github.com/ryanmcgrath/alchemy"
		},
		{
			"full_name": "izabera/zeromaps",
			"language": "C",
			"name": "zeromaps",
			"url": "https://github.com/izabera/zeromaps"
		},
		{
			"full_name": "tevora-threat/Scout",
			"language": "Vue",
			"name": "Scout",
			"url": "https://github.com/tevora-threat/Scout"
		}
	],
	"success": True
}
"""


def handle_data(data):
	#print(len(data))
	formatted_data = dict()
	for repo in data:
		lang = str(repo["language"])
		if lang == "None":
			continue
		if formatted_data.get(lang) == None:
			formatted_data[lang] = {
			"repos":[],
			"length":0,
			"language": lang
			}
		formatted_data[lang]["repos"].append(repo)
		formatted_data[lang]["length"] =len(
			formatted_data[lang]["repos"])
	#print(formatted_data.items())
	sorted_languages_names = sorted(formatted_data, 
		key=lambda item: formatted_data[item]["length"],
		reverse=True)
	handled_data = []
	for l_name in sorted_languages_names:
		handled_data.append(
			formatted_data[l_name])
	return handled_data





def handle_queries(queries,records):
	print("queries",queries,flush=True)
	#print("records",records,flush=True)
	#print("records",type(records),flush=True)
	# get the response from the URL
	#print("queries",queries)
	items = []
	#requests.get(q).json()["items"]
	for q in queries:
		requested_items = requests.get(q).json()["items"]
		for item in requested_items:
			item_data = {
				"url":item["html_url"],
				"name": item["name"],
				"full_name":item["full_name"],
				"language": item["language"]
				}
			items.append(item_data)
	return handle_data(items[0:records])


def github_search_repos(**kwargs):
	#print(kwargs)
	ser = GithubSearchRepoSerializer(data = kwargs)
	if not ser.is_valid():
		return {"success":False, "data":ser.errors}
	return {"success":True, 
	"data": handle_queries(ser.save(),
		ser.validated_data["records"])}


