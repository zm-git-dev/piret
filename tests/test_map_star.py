#! /usr/bin/env python
"""A suite to test file_exist."""
import os
import pytest
import luigi
from pypiret.Runs import Map
from plumbum.cmd import rm



def test_star():
        """Test star index creation, FaQC, and mapping."""
        luigi.interface.build([Map.star(fastqs=["tests/data/BTT_test15_R1.1000.fastq",
                                                "tests/data/BTT_test15_R2.1000.fastq"],
                      num_cpus=1,
                      fasta="tests/data2/chr22_ERCC92.fa",
                      stardb_dir="tests/test_star_mapping/index",
                      map_dir="tests/test_star_mapping/mapping_results",
                      gff_file="tests/data2/chr22_ERCC92.gff3",
                      sample="migun")], local_scheduler=True)
        assert os.path.exists("tests/test_star_mapping/mapping_results/migun_Aligned.sortedByCoord.out.bam") is True

        rm_cmd = rm["-rf", "tests/test_star_mapping"]
        rm_cmd()

