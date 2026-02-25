package com.random.sentences.service;

import java.util.logging.Logger;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.jms.core.JmsTemplate;

import com.random.sentences.model.RandomSentence;

@Service
public class SentenceService {

    private static final Logger log = Logger.getLogger(SentenceService.class.getName());
    private final String sentenceTopic = System.getenv("ACTIVEMQ_SENTENCE_TOPIC");

    @Autowired
    private JmsTemplate jmsTemplate;

    @SuppressWarnings("null")
    public String generateAndProcess() {
        String randomSentence = RandomSentence.generateRandomSentence();
        log.info(randomSentence);

        jmsTemplate.convertAndSend(sentenceTopic, randomSentence);
        log.info("Sent to AMQ Topic: " + sentenceTopic + "\nSentence: " + randomSentence);

        return randomSentence;
    }
    
}
