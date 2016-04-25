gem 'minitest', '>= 5.0.0'
require 'minitest/autorun'

class TestComputingGCcontent < MiniTest::Test
  def test_computing_for_dna_without_g_or_c_is_0
    assert_equal(0, compute_gc_content('ATATATA'))
  end

  def test_computing_for_dna_with_g_and_c_only_is_1
    assert_equal(100, compute_gc_content('GCCGCGCGCG'))
  end

  def test_computing_for_dna_with_all_4_symbols
    assert_equal(37.5, compute_gc_content('AGCTATAG'))
  end

  def test_real_input
    input = File.readlines('input.txt').map(&:strip)
    dna_strings = {}
    input.each_cons(2) do |id, strand|
      dna_strings[id] = compute_gc_content(strand)
    end
    best = dna_strings.values.max
    key = dna_strings.select { |id, gc_value| gc_value == best}.keys
    p best
    p key
  end
end

def compute_gc_content(dna_strand)
  gc_content = dna_strand.chars.select { |symbol| symbol =~ /[GC]/ }
  (gc_content.count.to_f / dna_strand.chars.count) * 100
end


input = File.readlines('input.txt').map(&:strip)
dna_strings = {}
input.each_cons(2) do |id, strand|
  dna_strings[id] = compute_gc_content(strand)
end
best = dna_strings.values.max
key = dna_strings.select { |id, gc_value| gc_value == best}.keys
p best
p key

  


