<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $sequence = $_POST["sequence"];

    // 시퀀스를 파일에 저장
    $queryFile = "query.fasta";
    file_put_contents($queryFile, $sequence);

    // blast 검색 실행
    $command = "blastp -query " . $queryFile . " -db prot_db -out result.txt";
    exec($command);

    // 결과 파일을 읽어와서 화면에 출력
    $resultFile = "result.txt";
    $result = file_get_contents($resultFile);

    echo "<pre>" . $result . "</pre>";
}
?>
