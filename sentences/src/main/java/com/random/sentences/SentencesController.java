package com.random.sentences;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.random.sentences.model.Words;
import com.random.sentences.model.WordsResponse;
import com.random.sentences.service.SentenceService;


@RestController
public class SentencesController {

    @Autowired 
    private SentenceService sentenceService;

    @GetMapping("/words")
    public WordsResponse getWords() {
        return new WordsResponse(
                Words.adjectivesList(),
                Words.nounsList(),
                Words.verbsList()
        );
    }

    @GetMapping("/random/sentence")
    public String getRandomSentence() {
        String randomSentence = sentenceService.generateAndProcess();
        return randomSentence;
    }

    @Scheduled(fixedRate = 5000)
    public void scheduledSentenceGeneration() {
        sentenceService.generateAndProcess();
    }
    
}
