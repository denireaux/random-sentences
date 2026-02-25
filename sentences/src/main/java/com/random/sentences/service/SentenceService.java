package com.random.sentences.service;

import java.util.logging.Logger;

import org.springframework.stereotype.Service;

import com.random.sentences.model.RandomSentence;

@Service
public class SentenceService {

    private static final Logger log = Logger.getLogger(SentenceService.class.getName());

    public String generateAndProcess() {
        String randomSentence = RandomSentence.generateRandomSentence();
        log.info(randomSentence);

        return randomSentence;
    }
    
}
