## **README**

### **프로젝트 설명**
이 Python 스크립트는 Excel 파일(`.xlsx`)에 저장된 단어와 의미를 읽어 음성 파일(`.mp3`)로 변환합니다. Google Text-to-Speech(`gTTS`) 및 `Pydub` 라이브러리를 활용하여, 한글과 영어를 각각 적절한 언어로 처리하며, 단어 사이에 사용자 정의 정지 시간을 추가합니다.

---

### **파일 구조**
```
project/
│
├── script.py              # Python 코드
├── example.xlsx           # Excel 파일 (입력 데이터)
└── file/output_with_pause.mp3  # 생성된 음성 파일
```

---

### **요구 사항**

#### **필수 라이브러리**
1. **gTTS**: 텍스트를 음성으로 변환.
2. **Pydub**: 음성 파일의 병합 및 조작.
3. **openpyxl**: Excel 파일 읽기.
4. **FFmpeg**: `Pydub`에서 음성 처리를 위한 필수 도구.

#### **설치 방법**
아래 명령어를 실행하여 필요한 라이브러리를 설치하세요:
```bash
pip3 install gtts pydub openpyxl
```

FFmpeg 설치가 필요합니다:
- **Linux**:
  ```bash
  sudo apt install ffmpeg
  ```
- **macOS**:
  ```bash
  brew install ffmpeg
  ```
- **Windows**:
  1. [FFmpeg 공식 사이트](https://ffmpeg.org/download.html)에서 Windows용 바이너리를 다운로드.
  2. 실행 파일 경로를 환경 변수에 추가.

---

### **사용 방법**

#### **1. Excel 파일 준비**
입력 Excel 파일(`.xlsx`)은 다음과 같은 형식을 가져야 합니다:
|  A  |       B       |       C       |
|-----|---------------|---------------|
|     | 영어 단어     | 한글 뜻       |
|  1  | resident      | 주민, 거주자  |
|  2  | manager       | 관리자, 경영자 |

- B 열: 영어 단어
- C 열: 한글 뜻

#### **2. 스크립트 실행**
1. 터미널에서 스크립트를 실행합니다:
   ```bash
   python script.py example.xlsx
   ```
   - `example.xlsx`는 입력 파일의 경로입니다.
   - 파일 경로는 스크립트 실행 시 명령행 인수로 제공해야 합니다.

2. 출력:
   - 입력 파일이 `example.xlsx`라면, 음성 파일이 `example.mp3`로 저장됩니다.
   - 음성 파일은 프로젝트 디렉토리의 `file` 폴더에 생성됩니다.

---

### **작동 원리**
1. **Excel 파일 읽기**:
   - `openpyxl`을 사용하여 Excel 파일에서 데이터를 읽습니다.
   - B 열(영어 단어)과 C 열(한글 뜻)을 `|`로 구분하여 문자열로 결합합니다.

2. **텍스트를 음성으로 변환**:
   - `gTTS`를 사용하여 각 단어를 음성으로 변환합니다.
   - 한글과 영어를 자동으로 감지하여 각각 `ko` 또는 `en`으로 처리합니다.

3. **단어 사이 정지 시간 추가**:
   - `Pydub`의 `AudioSegment.silent(duration=pause_duration)`을 사용하여 각 단어 사이에 정지 시간을 추가합니다.

4. **음성 파일 저장**:
   - 변환된 음성을 병합하여 최종 `.mp3` 파일로 저장합니다.

5. **임시 파일 삭제**:
   - 중간에 생성된 각 단어의 `.mp3` 파일은 최종 음성 파일 생성 후 삭제됩니다.

---

### **커스터마이징**

1. **정지 시간 변경**:
   - 단어 사이 정지 시간을 `pause_duration` 매개변수로 설정할 수 있습니다. 시간은 밀리초 단위로 설정됩니다.
   - 예: 2초(2000ms)로 변경:
     ```python
     text_to_speech_with_custom_pause(words, output_file="output_with_pause.mp3", pause_duration=2000)
     ```

2. **출력 경로 변경**:
   - 출력 파일 경로는 `output_file` 매개변수로 설정 가능합니다.
   - 기본적으로 입력 파일 이름에 `.mp3` 확장자가 붙은 이름으로 저장됩니다.

---

### **오류 처리**

1. **입력 파일이 없을 경우**:
   - 에러 메시지 출력:
     ```
     사용법: python script.py <파일경로>
     ```

2. **Excel 파일 형식 오류**:
   - Excel 파일이 올바른 형식(B, C 열 포함)이 아니면, 스크립트가 예상대로 동작하지 않을 수 있습니다.

3. **FFmpeg가 설치되지 않은 경우**:
   - `Pydub` 사용 중 오류 발생:
     ```
     Couldn’t find ffmpeg or avconv – defaulting to ffmpeg, but may not work
     ```
   - 해결: [FFmpeg 설치](#요구-사항).

---

### **예제**
#### **입력 데이터 (`example.xlsx`)**
|  A  |       B       |       C       |
|-----|---------------|---------------|
|     | 영어 단어     | 한글 뜻       |
|  1  | resident      | 주민, 거주자  |
|  2  | manager       | 관리자, 경영자 |

#### **출력**
- **파일명**: `example.mp3`
- **음성 내용**:
  ```
  resident (정지 시간) 주민, 거주자 (정지 시간) manager (정지 시간) 관리자, 경영자
  ```

---

### **라이선스**
이 프로젝트는 자유롭게 수정 및 배포할 수 있습니다. 단, `gTTS` 및 `Pydub`와 같은 라이브러리는 각자의 라이선스를 준수해야 합니다.