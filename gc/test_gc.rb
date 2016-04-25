gem 'minitest', '>= 5.0.0'
require 'minitest/autorun'


class TestComputingGCcontent < MiniTest::Test
  def test_computing_for_dna_without_g_or_c_is_0
    assert_equal(0, compute_gc_content('ATATATA'))
  end
end

def compute_gc_content(_)
  0
end
