"""User-set comparison scope: nominal targets plus V-ko siphta, 2026-11-14."""
# IDs remain in archival collections with explicit exclusions; never delete evidence.
CLAUSAL_IDS = {
 'K04','K17','K21','K23','K27','K32','K36','K37',
 'K45','K46','K49','K50','K51','K52','K53','K54','K55','K56',
}
VERSION='2026-11-14: nominal target realizations plus V-ko siphta only'
def annotate_scope(record):
 excluded=record['id'] in CLAUSAL_IDS
 record['comparison_scope_version']=VERSION
 record['comparison_eligible']=not excluded
 record['comparison_scope_reason']=(
  '外层目标内容以非名物化分句实现；用户排除 ko siphta 以外的分句形式'
  if excluded else
  '保留 ko siphta 愿望辅助结构' if record['id'] in {'K18','K19','K20'} else
  '目标内容为实体／事件名词或事件名物化 NP；载句的其他分句不作为其外层形式'
 )
 return record
