## **README**

### **프로젝트 설명**
이 프로젝트는 Python을 사용하여 텍스트 파일(`input_text.txt`)의 내용을 읽고, 이를 음성으로 변환하여 `.mp3` 파일로 저장하는 기능을 제공합니다. Google Text-to-Speech(`gTTS`)와 `Pydub` 라이브러리를 활용하며, 단어 사이에 사용자 정의 시간만큼의 일시 정지를 추가할 수 있습니다.

---

### **파일 구조**
```
project/
│
├── script.py              # Python 코드 (위 코드 저장)
├── input_text.txt         # 텍스트 파일 (음성으로 변환할 텍스트 포함)
└── output_with_pause.mp3  # 생성된 음성 파일 (실행 후 생성됨)
```

---

### **요구 사항**

#### **필요한 라이브러리**
1. **gTTS**: 텍스트를 음성으로 변환.
2. **Pydub**: 음성 파일의 조작 및 병합.
3. **FFmpeg**: `Pydub`에서 음성 처리를 위한 필수 도구.

#### **설치 방법**
아래 명령어를 사용해 필요한 라이브러리를 설치하세요:

```bash
pip install gtts pydub
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

1. **텍스트 파일 준비**:
   - 프로젝트 디렉토리 내에 `input_text.txt` 파일을 생성합니다.
   - 파일에 음성으로 변환할 텍스트를 입력합니다. 예:
     ```
     Hello how are you
     ```

2. **코드 실행**:
   - 터미널 또는 명령 프롬프트에서 다음 명령어를 실행:
     ```bash
     python script.py
     ```

3. **결과 확인**:
   - `output_with_pause.mp3` 파일이 생성됩니다.
   - 텍스트가 음성으로 변환되며, 각 단어 사이에 1초(1000ms)의 정적(무음)이 삽입됩니다.

---

### **커스터마이징**

1. **언어 변경**:
   - 기본 언어는 영어(`en`)로 설정되어 있습니다. 다른 언어를 사용하려면 `language` 매개변수를 변경하세요.
   - 예: 한국어로 변경:
     ```python
     text_to_speech_with_custom_pause(sample_text, language="ko", output_file="output_with_pause.mp3", pause_duration=1000)
     ```

2. **단어 사이 정지 시간**:
   - `pause_duration` 매개변수로 단어 사이의 정지 시간을 변경할 수 있습니다.
   - 시간은 밀리초 단위로 설정됩니다.
   - 예: 2초(2000ms)로 변경:
     ```python
     text_to_speech_with_custom_pause(sample_text, language="en", output_file="output_with_pause.mp3", pause_duration=2000)
     ```

---

### **출력 예제**

- **입력 텍스트**: `Hello how are you`
- **출력 음성 파일**: 
  - 파일 이름: `output_with_pause.mp3`
  - 음성: `"Hello"` (1초 정지) `"how"` (1초 정지) `"are"` (1초 정지) `"you"`

---

### **오류 처리**

1. **`input_text.txt` 파일이 없을 경우**:
   - 에러 메시지 출력:
     ```
     파일을 찾을 수 없습니다: input_text.txt
     ```

2. **FFmpeg가 설치되지 않은 경우**:
   - `Pydub` 사용 중 오류 발생:
     ```
     Couldn’t find ffmpeg or avconv – defaulting to ffmpeg, but may not work
     ```

   - 해결: [FFmpeg 설치](#요구-사항).

---

### **라이선스**
이 프로젝트는 자유롭게 수정 및 배포할 수 있습니다. 단, gTTS 및 Pydub와 같은 라이브러리는 각자의 라이선스를 준수해야 합니다.
