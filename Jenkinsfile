node{
    stage('clon-repo') {
    checkout scm
  }
  stage('SonarQube analysis') {
    def scannerHome = tool 'sonarqube';
    withSonarQubeEnv() { // If you have configured more than one global server connection, you can specify its name
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
  stage('Generate HTML Report') {
    // Directorio de salida del informe HTML
    def htmlReportDir = "${env.WORKSPACE}/html-reports"

    // Directorio donde se encuentran los archivos HTML que deseas generar
    def htmlFilesDir = "${env.WORKSPACE}/path/to/generate/html/files"

    // Genera los archivos HTML en el directorio especificado
    sh "mkdir -p ${htmlFilesDir}"
    sh "echo '<html><body><h1>HTML Report</h1><p>This is a sample report.</p></body></html>' > ${htmlFilesDir}/index.html"

    // Almacena los archivos en el área de almacenamiento temporal 'html-report' para compartirlos con la siguiente etapa
    stash(name: 'html-report', includes: "${htmlFilesDir}/**")
  }

  stage('Send Email') {
    // Extrae los archivos del área de almacenamiento temporal
    unstash('html-report')

    // Dirección de correo electrónico del destinatario
    def recipientEmail = 'iadiaz@unicesar.edu.co'

    // Asunto del correo electrónico
    def emailSubject = 'Informe HTML generado'

    // Cuerpo del correo electrónico
    def emailBody = 'Adjunto se encuentra el informe HTML generado.'

    // Ruta al archivo HTML que deseas adjuntar
    def htmlFilePath = "${env.WORKSPACE}/html-reports/index.html"

    // Envía el correo electrónico con el informe HTML adjunto
    emailext (
      to: recipientEmail,
      subject: emailSubject,
      body: emailBody,
      attachmentsPattern: htmlFilePath
    )
  }
}