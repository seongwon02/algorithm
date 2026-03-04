-- 코드를 작성해주세요
select d1.id as ID, d1.genotype as GENOTYPE, d2.genotype as PARENT_GENOTYPE
from ECOLI_DATA d1, ECOLI_DATA d2
where d1.parent_id = d2.id
and (d1.GENOTYPE & d2.GENOTYPE) = d2.genotype
order by id
