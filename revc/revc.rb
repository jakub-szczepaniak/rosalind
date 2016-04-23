class Revc
  DNA_COMPLEMENT = {
    'A' => 'T',
    'T' => 'A',
    'C' => 'G',
    'G' => 'C'
  }
  def self.complement(dna_strand)
    dna_strand.reverse.chars.map { |nucleotyde| DNA_COMPLEMENT[nucleotyde] }.join
  end
end

dataset = File.open('rosalind_revc.txt')
puts Revc.complement(dataset.read)


