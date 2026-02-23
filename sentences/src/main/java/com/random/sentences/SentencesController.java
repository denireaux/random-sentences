package com.random.sentences;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.random.sentences.model.Words;
import com.random.sentences.model.WordsResponse;


@RestController
public class SentencesController {

    @GetMapping("/words")
    public WordsResponse getWords() {
        return new WordsResponse(
                Words.adjectivesList(),
                Words.nounsList(),
                Words.verbsList()
        );
    }
}
