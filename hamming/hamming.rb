class Hamming
  VERSION = 1
  def self.compute(dna1, dna2)
    check_input(dna1, dna2)

    dna1.chars.zip(dna2.chars).count { |pair| differs(pair) }
  end

  def self.check_input(dna1, dna2)
    if dna1.length != dna2.length
      fail ArgumentError, 'DNA strands should have the same length!'
    end
  end

  def self.differs(nucleotyde_pair)
    nucleotyde_pair.first != nucleotyde_pair.last
  end
  private_class_method :check_input, :differs
end
