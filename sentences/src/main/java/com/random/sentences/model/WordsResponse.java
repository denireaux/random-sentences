package com.random.sentences.model;

import java.util.List;

public record WordsResponse(
        List<String> adjectives,
        List<String> nouns,
        List<String> verbs
) {}