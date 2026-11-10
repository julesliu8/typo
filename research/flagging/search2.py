exec(open('research/flagging/search.py').read().split('qs=')[0])
qs=['"want" "like" "happy" "case"','"desire" "emotion" "case frames"','"psychological predicates" "semantic map"','"experiencer" "flagging"','"psych predicates" "implicational"','"emotion predicates" "case marking"','"Experiencer" "valency classes"','"like" "want" "transitivity hierarchy"']
rs=list(concurrent.futures.ThreadPoolExecutor(max_workers=2).map(f,qs)) if 'f' in globals() else []
