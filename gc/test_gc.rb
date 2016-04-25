gem 'minitest', '>= 5.0.0'
require 'minitest/autorun'

class TestComputingGCcontent < MiniTest::Test
  def test_computing_for_dna_without_g_or_c_is_0
    assert_equal(0, compute_gc_content('ATATATA'))
  end

  def test_computing_for_dna_with_g_and_c_only_is_1
    assert_equal(1, compute_gc_content('GCCGCGCGCG'))
  end
end

def compute_gc_content(dna_strand)
  gc_content = dna_strand.chars.select { |symbol| symbol =~ /[GC]/ }
  gc_content.count / dna_strand.chars.count
end
