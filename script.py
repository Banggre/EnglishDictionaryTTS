import os
from gtts import gTTS
from pydub import AudioSegment

def read_text_from_file(file_path):
    """
    파일에서 텍스트를 읽어오는 함수.

    Args:
        file_path (str): 읽을 파일의 경로.

    Returns:
        str: 파일에서 읽은 텍스트.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {file_path}")
        return ""
    except Exception as e:
        print(f"오류 발생: {e}")
        return ""

def text_to_speech_with_custom_pause(text, output_file="output_with_pause.mp3", pause_duration=1000):
    """
    gTTS와 Pydub를 사용해 텍스트에 사용자 정의 쉬는 시간을 추가하는 함수.
    임시로 생성된 파일은 최종 파일 저장 후 삭제합니다.

    Args:
        text (str): 변환할 텍스트.
        language (str): 음성 언어 코드.
        output_file (str): 저장할 최종 음성 파일 이름.
        pause_duration (int): 단어 사이 쉬는 시간 (밀리초).

    Returns:
        None
    """
    try:
        # 텍스트를 단어로 나누기
        words = text.split()
        segments = []
        temp_files = []

        for i in range(len(words)):
            # 단어를 음성으로 변환
            word = words[i]
            tts = gTTS(text=word, lang="en" if i%2 ==0 else "ko", slow=False)
            word_audio = f"{word}.mp3"
            tts.save(word_audio)
            temp_files.append(word_audio)

            # 음성 파일을 AudioSegment로 읽기
            segments.append(AudioSegment.from_file(word_audio))

            # 단어 사이에 무음 추가
            segments.append(AudioSegment.silent(duration=pause_duration))

        # 모든 오디오 합치기
        final_audio = sum(segments)
        final_audio.export(output_file, format="mp3")
        print(f"음성 파일이 저장되었습니다: {output_file}")

        # 임시 파일 삭제
        for temp_file in temp_files:
            if os.path.exists(temp_file):
                os.remove(temp_file)
                print(f"임시 파일 삭제: {temp_file}")

    except Exception as e:
        print(f"오류 발생: {e}")

# 실행 예제
if __name__ == "__main__":
    # 텍스트를 읽어올 파일 경로
    text_file_path = "input_text.txt"

    # 파일에서 텍스트 읽기
    sample_text = read_text_from_file(text_file_path)
    mp3_file_path = text_file_path.replace(".txt", ".mp3")
    if sample_text:
        text_to_speech_with_custom_pause(sample_text, output_file = f"./file/{mp3_file_path}", pause_duration=1000)