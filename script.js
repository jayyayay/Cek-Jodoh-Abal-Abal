function nilaiNama(nama) {
  let total = 0;
  for (let huruf of nama.toLowerCase()) {
    if (/[a-z]/.test(huruf)) {
      total += huruf.charCodeAt(0) - 96;
    }
  }
  return total;
}

function zodiak(tanggal, bulan) {
  if ((bulan == 3 && tanggal >= 21) || (bulan == 4 && tanggal <= 19)) return "Aries";
  else if ((bulan == 4 && tanggal >= 20) || (bulan == 5 && tanggal <= 20)) return "Taurus";
  else if ((bulan == 5 && tanggal >= 21) || (bulan == 6 && tanggal <= 20)) return "Gemini";
  else if ((bulan == 6 && tanggal >= 21) || (bulan == 7 && tanggal <= 22)) return "Cancer";
  else if ((bulan == 7 && tanggal >= 23) || (bulan == 8 && tanggal <= 22)) return "Leo";
  else if ((bulan == 8 && tanggal >= 23) || (bulan == 9 && tanggal <= 22)) return "Virgo";
  else if ((bulan == 9 && tanggal >= 23) || (bulan == 10 && tanggal <= 22)) return "Libra";
  else if ((bulan == 10 && tanggal >= 23) || (bulan == 11 && tanggal <= 21)) return "Scorpio";
  else if ((bulan == 11 && tanggal >= 22) || (bulan == 12 && tanggal <= 21)) return "Sagittarius";
  else if ((bulan == 12 && tanggal >= 22) || (bulan == 1 && tanggal <= 19)) return "Capricorn";
  else if ((bulan == 1 && tanggal >= 20) || (bulan == 2 && tanggal <= 18)) return "Aquarius";
  else return "Pisces";
}

function hitungJodoh(nama1, nama2) {
  let nilai1 = nilaiNama(nama1);
  let nilai2 = nilaiNama(nama2);
  let selisih = Math.abs(nilai1 - nilai2);
  return 100 - (selisih % 50);
}

function cariJodoh100(nama1) {
  let target = nilaiNama(nama1);
  let nama2 = nama1;
  while (true) {
    let nilai2 = nilaiNama(nama2);
    if (Math.abs(target - nilai2) % 50 === 0) {
      return nama2;
    }
    nama2 += "a";
  }
}

document.getElementById("form-jodoh").addEventListener("submit", function(e) {
  e.preventDefault();

  const nama1 = document.getElementById("nama1").value;
  const tgl1 = parseInt(document.getElementById("tgl1").value);
  const bln1 = parseInt(document.getElementById("bln1").value);

  const nama2 = document.getElementById("nama2").value;
  const tgl2 = parseInt(document.getElementById("tgl2").value);
  const bln2 = parseInt(document.getElementById("bln2").value);

  const persen = hitungJodoh(nama1, nama2);
  const zod1 = zodiak(tgl1, bln1);
  const zod2 = zodiak(tgl2, bln2);

  let hasil = `===== HASIL =====
${nama1} (${zod1}) ❤️ ${nama2} (${zod2})
Kecocokan: ${persen}%\n`;

  if (persen < 50) {
    const rekomendasi = cariJodoh100(nama1);
    hasil += "😅 Wah, kurang cocok...\n";
    hasil += `💡 Saran nama pasangan yang cocok 100%: ${rekomendasi}\n`;
  } else if (persen > 85) {
    hasil += "Kalian ditakdirkan bersama 💍\n";
  } else if (persen > 70) {
    hasil += "Cinta kalian kuat 😍\n";
  } else {
    hasil += "Masih perlu usaha 🙂\n";
  }

  const quotes = [
    "Cinta sejati datang pada waktu yang tepat ❤️",
    "Jodoh tidak akan tertukar 💕",
    "Cinta butuh usaha dan kesabaran 💪",
    "Yang terbaik sedang menuju kamu ✨"
  ];
  hasil += "Quote: " + quotes[Math.floor(Math.random() * quotes.length)];

  document.getElementById("output").textContent = hasil;
});
