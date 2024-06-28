from youtube_transcript_api import YouTubeTranscriptApi
import re


# Function to retrieve the transcript of a YouTube video
def get_youtube_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join(item["text"] for item in transcript)
        return text
    except Exception as e:
        print(f"Error: {e}")
        return None


# Function for extractive summarization
def extractive_summarize(text, num_sentences=3):
    # Split the text into sentences
    sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", text)

    # Calculate the importance of each sentence based on sentence length
    sentence_lengths = [(sentence, len(sentence)) for sentence in sentences]

    # Sort sentences by importance (in this case, sentence length)
    sentence_lengths.sort(key=lambda x: x[1], reverse=True)

    # Select the top N important sentences for the summary
    summary_sentences = [sentence[0] for sentence in sentence_lengths[:num_sentences]]

    return " ".join(summary_sentences)


# Example usage
if __name__ == "__main__":
    video_id = "1DhawcqlpeM"  # Replace with the YouTube video ID
    num_sentences = 10  # Number of sentences in the summary
    transcript = get_youtube_transcript(video_id)

    if transcript:
        summary = extractive_summarize(transcript, num_sentences)
        print(summary)

        # Save the summary to a text file
        with open("msft.txt", "wb") as file:
            file.write(summary.encode("utf-8"))
        print("Summary saved to 'msft.txt'")
    else:
        print("Transcript not found or an error occurred.")
