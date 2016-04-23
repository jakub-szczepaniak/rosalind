#!/usr/bin/env ruby
gem 'minitest', '>= 5.0.0'
require 'minitest/autorun'
require_relative 'revc'

class RevcTest < Minitest::Test
  def test_with_four_elements
    assert_equal 'TGAC', Revc.complement('GTCA')
  end

  def test_with_four_elements_2
    assert_equal 'GTCA', Revc.complement('TGAC')
  end

  def test_whole_sample
    assert_equal 'AAAACCCGGT', Revc.complement('ACCGGGTTTT')
  end
end
