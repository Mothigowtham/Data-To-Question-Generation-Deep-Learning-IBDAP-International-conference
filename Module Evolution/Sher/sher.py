def sher(sher_ready):
    from sklearn.preprocessing import LabelEncoder
    from sklearn.metrics import f1_score
    import tensorflow as tf

    from sherlock import helpers
    from sherlock.features.preprocessing import extract_features, convert_string_lists_to_lists, prepare_feature_extraction
    from sherlock.deploy.train_sherlock import train_sherlock
    from sherlock.deploy.predict_sherlock import predict_sherlock
    import pandas as pd
    test_samples = pd.read_parquet('../data/data/raw/test_values.parquet')
    test_labels = pd.read_parquet('../data/data/raw/test_labels.parquet')

    test_samples_df2, y_test = convert_string_lists_to_lists(sher_ready, test_labels.iloc[0:20],"values", "type")
    X_test2 = extract_features(test_samples_df2)
    for i in range(0,1588):
        if( X_test2.iloc[:,i].dtype == bool):
            X_test2.iloc[:,i] = X_test2.iloc[:,i].astype(int)

    predicted_labels2 = predict_sherlock(X_test2, nn_id='sherlock')
    sher_pred = predicted_labels2.tolist()
    print ("Labels:", predicted_labels2)
    print (sher_pred)

	
    return sher_pred
