#!/usr/bin/env python

from omics_pipe.parameters.default_parameters import default_parameters
from omics_pipe.utils import *
p = Bunch(default_parameters)


def Varscan(sample, Varscan_flag):
    '''Calling variants with Varscan for whole genome sequencing.
        
        input:
        _gatk_recal.bam
        output:
        _varscan_somatic.4.1.vcf.gz
        citation:
        
        link:
        
        parameters from parameters file:
        
        TEMP_DIR:
        
        GENOME:
        
        SAMTOOLS_VERSION:
        
        VARSCAN_VERSION:
        
        CAPTURE_KIT_BED:
        
        ALIGNMENT_DIR:
        
        RESULTS:
        
        OPTIONS:
        '''
    if p.DNA["TUMOR_EXT"]:
        dna_tumor_sample = sample + p.DNA["TUMOR_EXT"]
    spawn_job(jobname = 'Varscan', SAMPLE = dna_tumor_sample, LOG_PATH = p.OMICSPIPE["LOG_PATH"], RESULTS_EMAIL = p.OMICSPIPE["EMAIL"], SCHEDULER = p.OMICSPIPE["SCHEDULER"], walltime = p.VARSCAN["WALLTIME"], queue = p.OMICSPIPE["QUEUE"], nodes = p.VARSCAN["NODES"], ppn = p.VARSCAN["CPU"], memory = p.VARSCAN["MEMORY"], script = "/Varscan.sh", args_list = [dna_tumor_sample, p.OMICSPIPE["TEMP_DIR"], p.VARSCAN["GENOME"], p.VARSCAN["SAMTOOLS_VERSION"], p.VARSCAN["VERSION"], p.VARSCAN["ALIGNMENT_DIR"], p.VARSCAN["RESULTS"], p.VARSCAN["OPTIONS"], p.VARSCAN["R_VERSION"], p.VARSCAN["VCFTOOLS_VERSION"], p.CAPTURE_KIT_BED])
    job_status(jobname = 'Varscan', resultspath = p.VARSCAN["RESULTS"] + "/" + dna_tumor_sample, SAMPLE = dna_tumor_sample,  outputfilename = dna_tumor_sample + "_varscan.4.1.vcf.gz", FLAG_PATH = p.OMICSPIPE["FLAG_PATH"])
    if p.DNA["NORMAL_EXT"]:
        dna_normal_sample = sample + p.DNA["NORMAL_EXT"]
    spawn_job(jobname = 'Varscan', SAMPLE = dna_normal_sample, LOG_PATH = p.OMICSPIPE["LOG_PATH"], RESULTS_EMAIL = p.OMICSPIPE["EMAIL"], SCHEDULER = p.OMICSPIPE["SCHEDULER"], walltime = p.VARSCAN["WALLTIME"], queue = p.OMICSPIPE["QUEUE"], nodes = p.VARSCAN["NODES"], ppn = p.VARSCAN["CPU"], memory = p.VARSCAN["MEMORY"], script = "/Varscan.sh", args_list = [dna_normal_sample, p.OMICSPIPE["TEMP_DIR"], p.VARSCAN["GENOME"], p.VARSCAN["SAMTOOLS_VERSION"], p.VARSCAN["VERSION"], p.VARSCAN["ALIGNMENT_DIR"], p.VARSCAN["RESULTS"], p.VARSCAN["OPTIONS"], p.VARSCAN["R_VERSION"], p.VARSCAN["VCFTOOLS_VERSION"], p.CAPTURE_KIT_BED])
    job_status(jobname = 'Varscan', resultspath = p.VARSCAN["RESULTS"] + "/" + dna_normal_sample, SAMPLE = dna_normal_sample,  outputfilename = dna_normal_sample + "_varscan.4.1.vcf.gz", FLAG_PATH = p.OMICSPIPE["FLAG_PATH"])
    return

if __name__ == '__main__':
   Varscan(sample, Varscan_flag)
   sys.exit(0)
